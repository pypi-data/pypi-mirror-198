from typing import Optional, List, Dict, Tuple, Union, Any

try:
    from questionary import unsafe_prompt, Separator, Style
    from questionary.prompts.common import print_formatted_text
    import questionary.constants
except ImportError as e:
    raise ImportError(f"Extra CLI dependencies not met: {str(e)}") from None

import re
from textwrap import wrap

from .task import TaskList, Task, TaskTree, TaskError
from .api import FetchMode


class PromptSeparator(Separator):
    def __init__(self) -> None:
        super().__init__('─' * 15)


_style: Style = Style(questionary.constants.DEFAULT_STYLE.style_rules + [
    ("aborting", "fg:ansibrightblack"),
    ("answer", "fg:ansibrightblue bold"),
    ("disabled", "fg:ansibrightblack"),
    ("highlighted", "fg:ansibrightblue"),
    ("instruction", "fg:ansibrightblack"),
    ("pointer", "fg:ansiyellow"),
    ("qmark", "fg:ansiyellow"),
    ("question", "bold"),
    ("selected", "fg:ansibrightblue"),
    ("separator", "fg:ansibrightblack"),
    ("text", ""),
    ("validation", "fg:ansibrightblue"),
])


def _get_term_width() -> Optional[int]:
    import os
    import sys
    import fcntl
    import struct

    try:
        return int(os.getenv("COLUMNS", None))  # type: ignore
    except (ValueError, TypeError):
        pass

    for fd in [sys.stdout.fileno(), sys.stderr.fileno()]:
        try:
            # TODO: handle SIGWINCH and cache
            ws_st: bytes = fcntl.ioctl(fd, 21523, b"\x00\x00" * 4)  # TIOCGWINSZ
            return struct.unpack("hhhh", ws_st)[1]  # ws_row, ws_col, ws_xpixel, ws_ypixel shorts
        except (OSError, struct.error):
            pass

    return None


def _style_str(class_name: str) -> Optional[str]:
    for class_names, style_str in reversed(_style.style_rules):
        if class_name in class_names.lower().split():
            return style_str
    return None


def print_err(text: str) -> None:
    print_formatted_text("! " + text, style=_style_str("aborting"))


def print_value(key: str, value: str) -> None:
    print_formatted_text("  " + key, style=_style_str("highlighted"), end=" ")
    print_formatted_text(value, style=_style_str("text"))


def print_text(text: Optional[str]) -> None:
    text = text.rstrip() if text is not None else ''
    columns: Optional[int] = _get_term_width()

    for line in text.splitlines(keepends=False):
        line = line.replace("\t", " " * 4).rstrip()
        indent: int = re.match(r"^[ >*+-]*", line).end()  # type: ignore
        for wrapped_line in wrap(line, width=columns,
                                 initial_indent="  ", subsequent_indent=" " * (2 + indent),
                                 replace_whitespace=True, drop_whitespace=False) if columns and line else ["  " + line]:
            print_formatted_text(wrapped_line, style=_style_str("text"))


def safe_prompt(questions: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
    try:
        return unsafe_prompt(questions, style=_style, **kwargs)
    except KeyboardInterrupt:
        print_err("Cancelled")
        return {}


def prompt_password() -> Optional[str]:
    answers: Dict = safe_prompt([{
        'type': 'password',
        'name': 'password',
        'message': 'Password',
    }])
    return answers.get('password', None)


def prompt_text(message: str, default: Optional[str] = None, validate: Optional[str] = None) -> Optional[str]:
    answers = safe_prompt([{
        'type': 'text',
        'name': 'content',
        'message': message,
        'default': default if default is not None else '',
        'validate': (lambda _: re.fullmatch(validate, _) is not None) if validate is not None else None
    }])
    return answers.get('content', '').strip() or None


def prompt_tasklist(lists: List[TaskList], default: Optional[TaskList] = None) -> Optional[Union[str, TaskList]]:
    menu: List[Union[Separator, Dict[str, Any]]] = [{'name': '[exit]', 'value': ''},
                                                    {'name': '[mode]', 'value': 'mode'},
                                                    {'name': 'Add list', 'value': 'new'},
                                                    PromptSeparator()]
    choices: List[Dict[str, Any]] = [{'name': _.name or "???", 'value': _} for _ in lists]

    default_index: int = 0
    if default is not None:
        for i, _ in enumerate(lists):
            if _.href == default.href:
                default_index = i
                break

    answers: Dict = safe_prompt([{
        'type': 'list',
        'name': 'tasklist',
        'message': 'Task list',
        'choices': [*menu, *choices],
        'default': choices[default_index] if 0 <= default_index < len(choices) else None
    }])
    return answers.get('tasklist', None) or None


def prompt_fetch_mode(default: FetchMode) -> FetchMode:
    answers: Dict = safe_prompt([{
        'type': 'list',
        'name': 'completed',
        'message': 'Task filter',
        'choices': [{'name': _.value, 'value': _} for _ in list(FetchMode)],
        'default': {'name': default.value, 'value': default}
    }])
    return answers.get('completed', default)


def prompt_task(tasks: TaskTree, default: Optional[int] = None) -> Optional[Union[str, Task]]:
    def task_label(d: int, t: Task) -> str:
        return "{} {} {}{}".format(
            '   ' * d,
            questionary.constants.INDICATOR_SELECTED if t.completed is not None else
            questionary.constants.INDICATOR_UNSELECTED,
            str(t.summary).strip(),
            ' […]' if t.description else '',
        )

    menu: List[Union[Separator, Dict[str, Any]]] = [{'name': '[back]', 'value': ''},
                                                    {'name': 'Add task', 'value': 'new'},
                                                    {'name': 'Rename list', 'value': 'edit'},
                                                    {'name': 'Delete list', 'value': 'delete'},
                                                    PromptSeparator()]
    try:
        choices: List[Dict[str, Any]] = [{'name': task_label(depth, task), 'value': task}
                                         for depth, task in tasks.tasks()]
    except (ValueError, KeyError) as e:
        raise TaskError(f"Cannot parse task for label: {str(e)}") from None

    answers: Dict = safe_prompt([{
        'type': 'list',
        'name': 'task',
        'message': 'Task',
        'choices': [*menu, *choices],
        'default': choices[default]
        if default is not None and 0 <= default < len(choices)
        else choices[0] if len(choices) else None,
    }, {
        'type': 'confirm',
        'when': lambda _: _.get('task', '') == 'delete',
        'name': 'confirm',
        'message': 'Confirm delete',
        'default': False,
    }])

    answer: Optional[Union[str, Task]] = answers.get('task', None) or None
    if isinstance(answer, str) and answer == 'delete':
        return answer if answers.get('confirm', False) else None
    else:
        return answer


def prompt_task_op() -> Optional[str]:
    answers: Dict = safe_prompt([{
        'type': 'list',
        'name': 'operation',
        'message': 'Edit task',
        'choices': [
            {'name': '[back]', 'value': ''},
            {'name': 'Toggle (un)completed', 'value': 'complete'},
            {'name': 'Edit task', 'value': 'edit'},
            {'name': 'Add subtask', 'value': 'subtask'},
            {'name': 'Delete task', 'value': 'delete'},
        ]
    }, {
        'type': 'confirm',
        'when': lambda _: _.get('operation', '') == 'delete',
        'name': 'confirm',
        'message': 'Confirm delete',
        'default': False,
    }])

    operation: Optional[str] = answers.get('operation', None) or None
    if operation == 'delete':
        return operation if answers.get('confirm', False) else None
    else:
        return operation


def prompt_content(content: Optional[str]) -> Optional[str]:
    answers = safe_prompt([{
        'type': 'text',  # editor
        'name': 'content',
        'message': 'First line summary, rest description',
        'default': content if content is not None else '',
        'multiline': True,
    }])

    new_content: str = answers.get('content', '').strip()
    if not new_content:
        return None
    elif content and new_content == content.strip():
        return None
    else:
        return new_content


def prompt_task_content(summary: Optional[str], description: Optional[str]) -> Tuple[Optional[str], Optional[str]]:
    content: Optional[str] = None
    if summary or description:
        content = "\n".join([
            summary or '',
            description or ''
        ])

    new_content: Optional[str] = prompt_content(content)
    if new_content is None:
        return None, None

    summary_desc: List[str] = new_content.split("\n", maxsplit=1)
    if len(summary_desc) > 1:
        return summary_desc[0].strip(), summary_desc[1].rstrip()
    else:
        return summary_desc[0].strip(), None
