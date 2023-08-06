# Nextcloud Tasks API

This library has been made available by [Hackitu.de](http://www.hackitu.de/nextcloud_tasks_api/).

It is published under the terms of the [GNU AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.html) licence.

Nextcloud tasks API and CLI
===========================

The default [Nextcloud Tasks App](https://github.com/nextcloud/tasks/ "Tasks app for Nextcloud") allows to manage task lists in calendars, which can be synced across devices via iCal todos. The corresponding WebGUI can be inconvenient for some use-cases or might not be exposed/reachable, so a console client that can work with tunnels or in an SSH sessions could come in handy. A library-like interface to the Nextcloud Tasks WebDAV API allows to use the core functionality also in the context of other projects or for automation.

As there seems to be no library specialized on Nextcloud tasks available yet, this project comes in three parts:

*   API class for WebDAV XML operations on task lists and tasks from a Nextcloud calendar
*   Interactive CLI client for browsing, managing, and editing tasks on a Nextcloud instance from the terminal (optional)
*   Simple custom iCal todo parser to work with tasks (optional)

Python Tasks API Quickstart[](#python_tasks_api_quickstart)
-----------------------------------------------------------

An API instance can be obtained by the convenience wrapper `get_nextcloud_tasks_api`. The following example snippet creates a new task and prints all tasks for all task lists found:

    api = get_nextcloud_tasks_api("https://my.nextcloud.com/", "username", "password")
    for task_list in api.get_lists():  # all task lists belonging to the authenticated user
        print(task_list.name)
    
        new_task = Task()  # empty iCal VTODO stub
        new_task.summary = "Test"
        new_task.completed = int(time.time())
        api.create(task_list, new_task.to_string())  # add (as completed) to task list
    
        for task in api.get_list(task_list):  # get all tasks in the list
            print(Task(task.content).summary)
    

### Endpoints[](#endpoints)

The following API operations are supported:

* `get_lists() -> Iterator[TaskList]`

    Find all available task lists.

* `get_list(task_list: TaskList, completed: Optional[bool]) -> Iterator[TaskFile]`

    Get all tasks of a task list, optionally filter remotely by completion state for performance reasons. Note that by default responses are streamed and parsed incrementally, so late exceptions can happen while iterating.

* `update_list(task_list: TaskList)`

    Update a list, i.e., with a new display name.

* `delete_list(task_list: TaskList)`

    Delete the given list.

* `create_list(filename: str, name: Optional[str]) -> TaskList`

    Create a new list with the given (unverified) filename and display name.

* `update(task: TaskFile) -> TaskFile`

    Update a task with its updated content.

* `delete(task: TaskFile)`

    Delete a task.

* `create(task_list: TaskList, task: str) -> TaskFile`

    Create a new task in the task list with the given iCal content.

### iCal Task Parser[](#ical_task_parser)

The API itself transparently operates on unparsed content – i.e., vCalendar/vEvent/iCal strings via XML/WebDAV – so any parsing approach can be used.

However, a simple [iCal parser](https://datatracker.ietf.org/doc/html/rfc5545#section-3.1 "RFC 5545 – iCalendar Specification")/factory as well as a `Task` class is included that can optionally be used for working with basic `VTODO` properties. More elaborate libraries with _todo_ support already exist on PyPI, for example [ical](https://pypi.org/project/ical/ "PyPI – ical: iCalendar rfc 5545 implementation in python >=3.9") or [iCal-library](https://pypi.org/project/ical-library/ "PyPI – ical-library: iCalendar reader with excellent recurrence support, RFC 5545 compliant").

Nextcloud Tasks Console Client[](#nextcloud_tasks_console_client)
-----------------------------------------------------------------

Based on the Nextcloud tasks API, an interactive CLI client for browsing, managing, and editing tasks is also included. This command-line client is optional, as its additional dependency ([`questionary`](https://pypi.org/project/questionary/ "PyPI – Questionary: Library for effortlessly building pretty command line interfaces")) is only included when the `cli` [extra](https://peps.python.org/pep-0508/#extras) is specified at installation time.

![Screenshot: Example task list view via CLI](doc/images/screenshot_dark_small.png "Screenshot: Example task list view via CLI")

On all found task lists, creating, (un-)completing, editing, and deleting tasks is supported, also for arbitrarily nested sub-tasks. In particular, guided by an interactive menu, you can:

*   Choose a task list from all lists found
*   Filter tasks by completion state
    *   Per default, all tasks are fetched to build up a tree structure that hides fully completed subtrees. For performance reasons or other use-cases, this can be changed to fetch and show all or only (un-)completed tasks.
*   See all tasks in a tree structure with a completed-indicator and their summary
*   Toggle completed states
*   Create a new task, possibly as child of an existing one
*   See or edit a task’s summary (“title”) and description
    *   Multiline descriptions are supported and [markdown bullet lists](https://daringfireball.net/projects/markdown/syntax#list "Markdown – Syntax: Lists") are consistently wrapped according to their indentation
*   Delete a task
*   Create, rename, or delete an entire task list

### Usage and Configuration[](#usage_and_configuration)

Simply run `nextcloud-tasks-api` with a configuration file:

```shell
usage: nextcloud-tasks-api \[-h\] \[-c CONFIG\]

Interactive CLI client for managing tasks on a Nextcloud instance.

optional arguments:
  -h, --help  show this help message and exit
  -c CONFIG   configuration file, in .ini or .json format (default: ./tasks\_config.ini)

```
The config file consists of simple key/value pairs and will be read from `tasks_config.ini` in the current directory if not specified otherwise. In [INI format](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure "Python documentation – Configuration file parser"), it should contain a single (arbitrarily named) section with the following keys. Alternatively, a `.json` file with a corresponding dictionary can be given.

`base_url`

URL of the instance, gets the API calls appended, for example: `https://my.nextcloud.com/`

`username`

Username to login with.

`password`

Password to login with. Using an [App Password](https://docs.nextcloud.com/server/latest/user_manual/en/session_management.html#managing-devices "Nextcloud User Manual – Manage connected browsers and devices") instead of the main account password should be considered. Adding an App Password is also needed when the account has 2FA enabled.

`password_type`

Either `plain` (default) or `openssl-aes`, the latter for an encrypted password which requires the `openssl` binary. A compatible [encryption](https://wiki.openssl.org/index.php/Enc "OpenSSLWiki – Command line tools for encryption and decryption") step is for example:  
`echo -n "nextcloud-password" | openssl enc -e -aes-256-cbc -salt -pbkdf2 -base64`  
This will prompt for a password that then needs to be given to the CLI at startup.

`verify_ssl`

Verify the SSL certificate of an HTTPS API URL, enabled per default.


