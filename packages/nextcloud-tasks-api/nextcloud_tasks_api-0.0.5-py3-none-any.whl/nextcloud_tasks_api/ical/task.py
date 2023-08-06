from typing import Optional

from .ical import ICalParser, ICal


class Task:
    """
    A task as given by the vCalendar/vEvent/iCal payload to parse.
    Not used by the API which operates on unparsed content, so its usage is optional when no further handling is needed.
    Intended as minimal builtin implementation -- more elaborate libraries exist.
    Note that the convenience getter/setter proxies silently ignore iCal 'parameters' and assume UTC timestamps.
    """

    def __init__(self, data: Optional[str] = None) -> None:
        """Parse content obtained from the API."""
        if data is None:
            self._caldav: ICal = ICalParser.create()
        else:
            self._caldav = ICalParser.from_string(data)  # ValueError

    def to_string(self) -> str:
        """Give content to be passed to the API."""
        return ICalParser.to_string(self._caldav)

    @property
    def data(self) -> ICal:
        """Direct access to the parsed iCal datastructure, without using the convenience getter/setter proxies below."""
        return self._caldav

    @property
    def uid(self) -> Optional[str]:
        return self._caldav.find_value("UID")

    @property
    def related_to(self) -> Optional[str]:
        return self._caldav.find_value("RELATED-TO")

    @related_to.setter
    def related_to(self, uid: str) -> None:
        self._caldav.upsert_value("RELATED-TO", uid if uid else None)

    @property
    def summary(self) -> Optional[str]:
        return self._caldav.find_value("SUMMARY")

    @summary.setter
    def summary(self, value: str) -> None:
        self._caldav.upsert_value("SUMMARY", value)

    @property
    def description(self) -> Optional[str]:
        return self._caldav.find_value("DESCRIPTION")

    @description.setter
    def description(self, value: Optional[str]) -> None:
        self._caldav.upsert_value("DESCRIPTION", value if value is not None else None)

    @property
    def created(self) -> Optional[int]:
        ts: Optional[str] = self._caldav.find_value("CREATED")
        return ICalParser.parse_timestamp(ts) if ts is not None else None

    @created.setter
    def created(self, value: int) -> None:
        self._caldav.upsert_value("CREATED", ICalParser.from_timestamp(value))

    @property
    def last_modified(self) -> Optional[int]:
        ts: Optional[str] = self._caldav.find_value("LAST-MODIFIED")
        return ICalParser.parse_timestamp(ts) if ts is not None else None

    @last_modified.setter
    def last_modified(self, value: int) -> None:
        self._caldav.upsert_value("LAST-MODIFIED", ICalParser.from_timestamp(value))

    @property
    def completed(self) -> Optional[int]:
        ts: Optional[str] = self._caldav.find_value("COMPLETED")
        return ICalParser.parse_timestamp(ts) if ts is not None else None

    @completed.setter
    def completed(self, value: Optional[int]) -> None:
        self._caldav.upsert_value("COMPLETED", ICalParser.from_timestamp(value) if value is not None else None)
        self._caldav.upsert_value("PERCENT-COMPLETE", "100" if value is not None else None)
        self._caldav.upsert_value("STATUS", "COMPLETED" if value is not None else None)
