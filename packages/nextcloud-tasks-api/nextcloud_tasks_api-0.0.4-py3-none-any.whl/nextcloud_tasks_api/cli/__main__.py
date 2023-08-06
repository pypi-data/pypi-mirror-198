"""
Interactive CLI client for browsing, managing, and editing tasks on a Nextcloud instance.
"""

from typing import Optional

import sys
import argparse
from subprocess import run, SubprocessError
from tempfile import NamedTemporaryFile

from nextcloud_tasks_api import NextcloudTasksApi, get_nextcloud_tasks_api
from .config import Config, ConfigError
from .prompts import print_err, prompt_password
from .api import TasksApi
from .cli import cli_main


def _decrypt(encrypted: str, password: str) -> Optional[str]:
    with NamedTemporaryFile("w", delete=True) as pass_file:
        pass_file.write(password)  # don't expose password in subprocess arguments
        pass_file.flush()
        try:
            # echo -n "nextcloud-password" | openssl enc -e -aes-256-cbc -salt -pbkdf2 -base64
            proc = run(["openssl", "enc", "-d",
                        "-aes-256-cbc", "-salt", "-pbkdf2", "-base64",
                        "-pass", f"file:{pass_file.name}"],
                       input=f"{encrypted}\n",
                       capture_output=True,
                       encoding="utf-8", errors="strict",
                       check=True)
        except (SubprocessError, UnicodeError) as e:
            print_err(f"Cannot decrypt password: {str(e)}")
            return None
        else:
            return proc.stdout


def _get_password(config: Config) -> Optional[str]:
    if config.password_type == "openssl-aes":
        passphrase: Optional[str] = prompt_password()
        if passphrase is None:
            print_err("Cannot decrypt password: No passphrase given")
            return None
        return _decrypt(config.password, passphrase)
    else:
        return config.password


def _main(config: Config) -> bool:
    password: Optional[str] = _get_password(config)
    if password is None:
        return False
    api: NextcloudTasksApi = get_nextcloud_tasks_api(base_url=config.base_url,
                                                     username=config.username, password=password,
                                                     verify_ssl=config.verify_ssl,
                                                     stream=True)
    return cli_main(TasksApi(api))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip(),
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', type=str, metavar="CONFIG", default="./tasks_config.ini",
                        help="configuration file, in .ini or .json format")
    args = parser.parse_args()

    try:
        config: Config = Config.from_file(args.c)
    except ConfigError as e:
        print_err(f"Cannot load config from '{args.c}': {str(e)}")
        return 1
    else:
        return 0 if _main(config) else 1


if __name__ == "__main__":
    sys.exit(main())
