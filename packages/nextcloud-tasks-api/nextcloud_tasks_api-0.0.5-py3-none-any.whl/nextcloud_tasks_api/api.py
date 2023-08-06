from typing import Optional, Iterator

from urllib.parse import quote as url_quote
from pathlib import PurePath
from uuid import uuid4

from .request import Requester, Request, Response
from .parser import DavParser
from .error import ApiError


class TaskList:
    """Handle of a task list returned by the API."""

    def __init__(self, href: PurePath, name: Optional[str]) -> None:
        self._href: PurePath = href
        self._name: Optional[str] = name

    @property
    def href(self) -> PurePath:
        return self._href

    @property
    def name(self) -> Optional[str]:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name


class TaskFile:
    """Handle of a particular task of a task list returned by the API."""

    def __init__(self, href: PurePath, etag: Optional[str], content: str) -> None:
        self._href: PurePath = href
        self._etag: Optional[str] = etag
        self._content: str = content  # vCalendar/vEvent/iCal payload

    @property
    def href(self) -> PurePath:
        return self._href

    @property
    def etag(self) -> Optional[str]:
        return self._etag

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str) -> None:
        self._content = content


class NextcloudTasksApi:
    """Main interface, using a backend for XML DAV requests and working with ICAL data."""

    def __init__(self, requester: Requester) -> None:
        self._requester: Requester = requester
        self._parser: DavParser = DavParser()

    def get_lists(self) -> Iterator[TaskList]:
        """Find all available task lists."""

        response: Response = self._requester.request(Request(
            method="PROPFIND",
            url="/remote.php/dav/calendars/{}/".format(url_quote(self._requester.username, safe='')),
            headers={"Content-Type": "application/xml; charset=utf-8"},
            content=self._parser.get_propfind_calendars(),
        ))
        response.raise_for(207, "application/xml; charset=utf-8")

        for href, name in self._parser.parse_list_for_calendars(response.content):
            yield TaskList(href=PurePath(href), name=name)

    def get_list(self, task_list: TaskList, completed: Optional[bool] = None) -> Iterator[TaskFile]:
        """Get all tasks of a tasklist, optionally filter remotely by completion state for performance reasons."""

        response: Response = self._requester.request(Request(
            method="REPORT",
            url=task_list.href.as_posix(),
            headers={"Content-Type": "application/xml; charset=utf-8", "Depth": "1"},
            content=self._parser.get_report_calendar(completed),
        ))
        response.raise_for(207, "application/xml; charset=utf-8")

        for href, etag, caldav in self._parser.parse_get_for_calendar(response.content):
            yield TaskFile(href=PurePath(href), etag=etag, content=caldav)

    def update_list(self, task_list: TaskList) -> None:
        """Update a list with its updated handle."""

        response: Response = self._requester.request(Request(
            method="PROPPATCH",
            url=task_list.href.as_posix(),
            headers={"Content-Type": "application/xml; charset=utf-8", "Depth": "0"},
            content=self._parser.get_property_update(task_list.name if task_list.name is not None
                                                     else task_list.href.stem)
        ))
        response.raise_for(207, "application/xml; charset=utf-8")
        if list(self._parser.parse_propstat_for_status(response.content)) != [task_list.href.as_posix()]:
            raise ApiError(f"Cannot update tasklist '{task_list.href}'") from None

    def delete_list(self, task_list: TaskList) -> None:
        """Delete the given list."""

        response: Response = self._requester.request(Request(
            method="DELETE",
            headers={"Depth": "0"},
            url=task_list.href.as_posix(),
        ))
        response.raise_for(204)
        response.content.close()

    def create_list(self, filename: str, name: Optional[str] = None) -> TaskList:
        """Create a new list with the given (unverified) filename and displayname."""

        url: PurePath = PurePath("/remote.php/dav/calendars") / \
            url_quote(self._requester.username, safe='') / \
            url_quote(filename, safe='')

        response: Response = self._requester.request(Request(
            method="MKCOL",
            url=url.as_posix(),
            headers={"Content-Type": "application/xml; charset=utf-8", "Depth": "0"},
            content=self._parser.get_mkcol_calendar(name if name is not None else filename),
        ))
        response.raise_for(201)
        response.content.close()
        return TaskList(href=url, name=name if name is not None else filename)

    def update(self, task: TaskFile) -> TaskFile:
        """Update a task with its updated content."""

        response: Response = self._requester.request(Request(
            method="PUT",
            url=task.href.as_posix(),
            headers={**{"Content-Type": "text/calendar; component=vtodo; charset=utf-8"},
                     **({"If-Match": task.etag} if task.etag is not None else {})},
            content=task.content.encode(encoding="utf-8", errors="strict"),
        ))
        response.raise_for(204)
        response.content.close()
        return self._get_task(task.href)  # for new etag

    def delete(self, task: TaskFile) -> None:
        """Delete a task."""

        response: Response = self._requester.request(Request(
            method="DELETE",
            headers={"If-Match": task.etag} if task.etag is not None else {},
            url=task.href.as_posix(),
        ))
        response.raise_for(204)
        response.content.close()

    def create(self, task_list: TaskList, task: str) -> TaskFile:
        """Create a new task in the task list with the given iCal content."""

        href: PurePath = task_list.href / PurePath(str(uuid4()).upper()).with_suffix(".ics")
        response: Response = self._requester.request(Request(
            method="PUT",
            url=href.as_posix(),
            headers={"Content-Type": "text/calendar; charset=utf-8"},
            content=task.encode(encoding="utf-8", errors="strict"),
        ))
        response.raise_for(201)
        response.content.close()
        return self._get_task(href)

    def _get_task(self, task_href: PurePath) -> TaskFile:
        response: Response = self._requester.request(Request(
            method="PROPFIND",
            url=task_href.as_posix(),
            headers={"Content-Type": "application/xml; charset=utf-8"},
            content=self._parser.get_propfind_calendar(),
        ))
        response.raise_for(207, "application/xml; charset=utf-8")

        try:
            href, etag, caldav = next(self._parser.parse_get_for_calendar(response.content))
            response.content.close()
            return TaskFile(href=PurePath(href), etag=etag, content=caldav)
        except StopIteration:
            raise ApiError(f"Cannot get task '{task_href}'") from None
