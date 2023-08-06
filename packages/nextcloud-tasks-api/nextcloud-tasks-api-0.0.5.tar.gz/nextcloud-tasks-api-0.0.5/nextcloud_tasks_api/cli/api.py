from typing import List, Optional
from enum import Enum

from nextcloud_tasks_api import NextcloudTasksApi
from .task import TaskList, Task, TaskTree, TaskError


class FetchMode(Enum):
    auto = 'Auto'  # fetch all but filter afterwards, this allows completed parents with uncompleted subtasks
    uncompleted = 'Uncompleted only'
    completed = 'Completed only'
    all = 'All'


class TasksApi:
    """Wraps the actual NextcloudTasksApi with a parsed Task and TaskTree, merely proxies TaskList operations."""

    def __init__(self, api: NextcloudTasksApi) -> None:
        self._api: NextcloudTasksApi = api

    def get_lists(self) -> List[TaskList]:
        return list(self._api.get_lists())

    def get_list(self, task_list: TaskList, mode: FetchMode) -> TaskTree:
        fetch_completed: Optional[bool] = None if mode in {FetchMode.auto, FetchMode.all} else \
            mode in {FetchMode.completed}
        filter_completed: bool = mode in {FetchMode.auto}

        tasks = self._api.get_list(task_list, fetch_completed)
        return TaskTree((Task(taskdef) for taskdef in tasks), filter_completed)

    def update_list(self, task_list: TaskList) -> None:
        self._api.update_list(task_list)

    def delete_list(self, task_list: TaskList) -> None:
        self._api.delete_list(task_list)

    def create_list(self, name: str) -> TaskList:
        return self._api.create_list(name)

    def update(self, task: Task) -> Task:
        try:
            return Task(self._api.update(task.ctx))
        except (ValueError, KeyError) as e:
            raise TaskError(f"Cannot parse task to update: {str(e)}") from None

    def delete(self, task: Task) -> None:
        try:
            self._api.delete(task.ctx)
        except (ValueError, KeyError) as e:
            raise TaskError(f"Cannot parse task to delete: {str(e)}") from None

    def create(self, task_list: TaskList, task: Task) -> Task:
        try:
            return Task(self._api.create(task_list, task.to_string()))
        except (ValueError, KeyError) as e:
            raise TaskError(f"Cannot parse task to create in '{task_list.name}': {str(e)}") from None
