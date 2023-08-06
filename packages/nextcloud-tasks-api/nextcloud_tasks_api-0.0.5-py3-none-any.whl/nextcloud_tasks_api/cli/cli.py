from typing import Optional, List, Union, Tuple

from time import time
from datetime import datetime

from nextcloud_tasks_api import ApiError
from .api import TasksApi, FetchMode
from .task import TaskList, Task, TaskTree, TaskError
from .prompts import print_err, print_value, print_text
from .prompts import prompt_tasklist, prompt_fetch_mode, prompt_task, prompt_task_op, prompt_task_content, prompt_text


def _do_tasklists(api: TasksApi) -> bool:
    default_list: Optional[TaskList] = None
    fetch_mode: FetchMode = FetchMode.auto
    while True:
        task_lists: List[TaskList] = api.get_lists()
        task_list: Optional[Union[str, TaskList]] = prompt_tasklist(task_lists, default_list)
        if task_list is None:
            return True
        elif isinstance(task_list, TaskList):
            default_list = task_list
            if not _do_tasklist(api, fetch_mode, task_list):
                return False
        elif isinstance(task_list, str) and task_list == 'mode':
            fetch_mode = prompt_fetch_mode(fetch_mode)
        elif isinstance(task_list, str) and task_list == 'new':
            default_list = _create_tasklist(api) or default_list


def _do_tasklist(api: TasksApi, fetch_mode: FetchMode, tasklist: TaskList) -> bool:
    last: Optional[Tuple[Task, Optional[int]]] = None
    while True:
        tasks: TaskTree = api.get_list(tasklist, fetch_mode)
        while True:
            default: Optional[int] = None
            if last is not None:
                default = tasks.index(last[0])
                if default is None:
                    default = last[1]

            task: Optional[Union[str, Task]] = prompt_task(tasks, default=default)

            if task is None:
                return True
            elif isinstance(task, Task):
                last = task, tasks.index(task)
                _print_task(task)
                if _do_task(api, tasklist, task):
                    break
            elif isinstance(task, str) and task == 'new':
                new_task: Optional[Task] = _create_task(api, tasklist, None)
                if new_task is not None:
                    last = new_task, None
                    break
            elif isinstance(task, str) and task == 'edit':
                name: Optional[str] = prompt_text("Tasklist name", tasklist.name)
                if name is not None and name != tasklist.name:
                    tasklist.name = name
                    api.update_list(tasklist)
            elif isinstance(task, str) and task == 'delete':
                api.delete_list(tasklist)
                return True


def _do_task(api: TasksApi, tasklist: TaskList, task: Task) -> bool:
    operation: Optional[str] = prompt_task_op()
    if operation is None:
        return False
    elif operation == 'subtask':
        return _create_task(api, tasklist, task) is not None
    elif operation == 'complete':
        return _complete_task(api, task) is not None
    elif operation == 'edit':
        return _edit_task(api, task) is not None
    elif operation == 'delete':
        api.delete(task)
        return True
    else:
        return False


def _complete_task(api: TasksApi, task: Task) -> Task:
    try:
        task.completed = int(time()) if task.completed is None else None
        task.apply()
    except (ValueError, KeyError) as e:
        raise TaskError(f"Cannot update task: {str(e)}") from None
    else:
        return api.update(task)


def _create_task(api: TasksApi, tasklist: TaskList, parent: Optional[Task]) -> Optional[Task]:
    summary, description = prompt_task_content(None, None)
    if summary is None:
        return None

    try:
        parent_uid: Optional[str] = parent.uid if parent is not None else None
        task: Task = Task(None)
        task.summary = summary
        if description is not None:
            task.description = description
        if parent_uid is not None:
            task.related_to = parent_uid
    except (ValueError, KeyError) as e:
        raise TaskError(f"Cannot create task: {str(e)}") from None
    else:
        return api.create(tasklist, task)  # no apply


def _create_tasklist(api: TasksApi) -> Optional[TaskList]:
    name: Optional[str] = prompt_text("Tasklist name", validate="[a-zA-Z0-9 _-]*")
    if name is None:
        return None
    try:
        return api.create_list(name)
    except ApiError as e:
        print_err(str(e))
        return None


def _print_task(task: Task) -> None:
    def format_time(ts: Optional[int]) -> str:
        return datetime.fromtimestamp(ts).isoformat(sep=" ") if ts is not None else "-"

    try:
        print_text(task.description)
        print_value("Created  ", format_time(task.created))
        print_value("Modified ", format_time(task.last_modified))
        print_value("Completed", format_time(task.completed))
    except (ValueError, KeyError) as e:
        print_err(f"Cannot parse task: {str(e)}")
        return


def _edit_task(api: TasksApi, task: Task) -> Optional[Task]:
    try:
        summary, description = prompt_task_content(task.summary, task.description)
    except (ValueError, KeyError) as e:
        raise TaskError(f"Cannot parse task: {str(e)}") from None
    else:
        if summary is None:
            return None

    try:
        task.summary = summary
        task.description = description
        task.last_modified = int(time())
        task.apply()
    except (ValueError, KeyError) as e:
        raise TaskError(f"Cannot update task: {str(e)}") from None
    else:
        return api.update(task)


def cli_main(api: TasksApi) -> bool:
    try:
        return _do_tasklists(api)
    except (ApiError, TaskError) as e:
        print_err(f"{type(e)}: {str(e)}")
        return False
