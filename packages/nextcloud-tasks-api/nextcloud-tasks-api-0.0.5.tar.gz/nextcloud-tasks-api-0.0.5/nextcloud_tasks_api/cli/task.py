from typing import List, Tuple, Optional, Iterator, Iterable

from nextcloud_tasks_api import TaskFile, TaskList as ApiTaskList
from nextcloud_tasks_api.ical import Task as ApiTask


class TaskError(Exception):
    pass


TaskList = ApiTaskList


class Task(ApiTask):
    def __init__(self, ctx: Optional[TaskFile]) -> None:
        try:
            super().__init__(ctx.content if ctx is not None else None)
            self._ctx: Optional[TaskFile] = ctx
        except (ValueError, KeyError) as e:
            raise TaskError(f"Cannot parse task from '{type(ctx)}': {str(e)}")

    def apply(self) -> None:
        self.ctx.content = self.to_string()

    @property
    def ctx(self) -> TaskFile:
        if self._ctx is None:
            raise TaskError("Task not bound to an API object")
        return self._ctx


class TaskTree:
    class Node:
        def __init__(self, task: Task) -> None:
            self.task: Task = task
            self.children: List[TaskTree.Node] = []

        def _find(self, uid: str) -> Optional['TaskTree.Node']:
            if self.task.uid == uid:
                return self
            return self.find(self.children, uid)

        @classmethod
        def find(cls, nodes: List['TaskTree.Node'], uid: str) -> Optional['TaskTree.Node']:
            for child in nodes:
                found: Optional[TaskTree.Node] = child._find(uid)
                if found is not None:
                    return found
            return None

        def _sort(self) -> None:
            self.children.sort(key=lambda n: n.task.summary.lower() if n.task.summary else '')
            for child in self.children:
                child._sort()

        @classmethod
        def sort(cls, nodes: List['TaskTree.Node']) -> None:
            nodes.sort(key=lambda n: n.task.summary.lower() if n.task.summary else '')
            for node in nodes:
                node._sort()

        @property
        def completed(self) -> Optional[bool]:
            is_completed: bool = self.task.completed is not None
            for child in self.children:
                if child.completed != is_completed:
                    return None  # mixed
            else:
                return is_completed

        def dump(self, exclude_completed: bool, depth: int = 0) -> Iterator[Tuple[int, Task]]:
            if exclude_completed and self.completed is True:
                return
            else:
                yield depth, self.task
            for child in self.children:
                yield from child.dump(exclude_completed, depth + 1)

    def __init__(self, tasks: Iterable[Task], exclude_completed: bool) -> None:
        self._exclude_completed: bool = exclude_completed
        self._tree: List[TaskTree.Node] = self._build_tree(tasks)
        self._tasks: List[Tuple[int, Task]] = list(self._dump())

    def tasks(self) -> Iterator[Tuple[int, Task]]:
        yield from self._tasks

    def index(self, task: Task) -> Optional[int]:
        try:
            index: int = 0
            for _, node in self.tasks():
                if node.uid == task.uid:
                    return index
                index += 1
            return None
        except (ValueError, KeyError) as e:
            raise TaskError(f"Cannot find task uid: {str(e)}") from None

    def _dump(self) -> Iterator[Tuple[int, Task]]:
        try:
            for node in self._tree:
                yield from node.dump(self._exclude_completed)
        except (ValueError, KeyError) as e:
            raise TaskError(f"Cannot list tasks: {str(e)}") from None

    @classmethod
    def _build_tree(cls, tasks: Iterable[Task], sort: bool = True) -> List['TaskTree.Node']:
        tree: List[TaskTree.Node] = [TaskTree.Node(_) for _ in tasks]  # need to buffer all to find late parents
        try:
            for node in list(tree):  # duplicate and change in-place
                related_to: Optional[str] = node.task.related_to
                if related_to is not None:
                    parent: Optional[TaskTree.Node] = TaskTree.Node.find(tree, related_to)
                    if parent is not None:
                        parent.children.append(node)
                        tree.remove(node)
            if sort:
                TaskTree.Node.sort(tree)
        except (ValueError, KeyError) as e:
            raise TaskError(f"Cannot build task tree: {str(e)}") from None
        return tree
