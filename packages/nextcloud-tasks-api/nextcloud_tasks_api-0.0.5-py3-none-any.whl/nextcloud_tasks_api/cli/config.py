from typing import Dict
from dataclasses import dataclass, fields

import json
import configparser


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class Config:
    """
    Configuration file, parsed from either a single .ini section or a .json dictionary.
    base_url: URL of the instance, gets the API calls appended, for example: 'https://my.nextcloud.com/'
    username: Username to login with.
    password: Password to login with, using an 'App Password' instead of the main account password should be considered.
    password_type: Either 'plain' or 'openssl-aes', the latter for an encrypted password in the config. Encrypt with:
                   `echo -n "nextcloud-password" | openssl enc -e -aes-256-cbc -salt -pbkdf2 -base64`
                   This prompts for an encryption password that then needs to be given to the CLI at startup.
    verify_ssl: Verify the SSL certificate of an HTTPS API URL, enabled per default.
    """

    base_url: str
    username: str
    password: str
    password_type: str = 'plain'
    verify_ssl: bool = True

    def __post_init__(self) -> None:
        for f in fields(self):
            if not isinstance(getattr(self, f.name), f.type):
                if f.type is bool:
                    super().__setattr__(f.name, self._to_bool(getattr(self, f.name)))
                else:
                    raise ConfigError(f"Invalid '{f.name}' type")
        if not self.base_url.startswith(("http://", "https://")):
            raise ConfigError(f"Invalid URL '{self.base_url}'")
        if self.password_type not in {"plain", "openssl-aes"}:
            raise ConfigError(f"Invalid password type '{self.password_type}'")

    @classmethod
    def _to_bool(cls, value) -> bool:
        try:
            return configparser.RawConfigParser.BOOLEAN_STATES[value]
        except (ValueError, KeyError):
            raise ConfigError(f"Invalid boolean value '{value}'")

    @classmethod
    def from_dict(cls, config: Dict) -> 'Config':
        if not isinstance(config, dict):
            raise ConfigError("Expecting config dict")
        try:
            return cls(**config)
        except TypeError as e:
            raise ConfigError(str(e)) from None

    @classmethod
    def from_json(cls, filename: str) -> 'Config':
        try:
            with open(filename, "r") as fp:
                return cls.from_dict(json.load(fp))
        except (OSError, json.JSONDecodeError, UnicodeDecodeError) as e:
            raise ConfigError(str(e)) from None

    @classmethod
    def from_ini(cls, filename: str) -> 'Config':
        parser: configparser.ConfigParser = configparser.ConfigParser()
        try:
            with open(filename, "r") as fp:
                parser.read_file(fp)
        except (OSError, configparser.Error, UnicodeDecodeError) as e:
            raise ConfigError(str(e)) from None
        if len(parser.sections()) != 1:
            raise ConfigError("Expecting single ini section")
        else:
            return cls.from_dict({k: v for k, v in parser.items(parser.sections()[0])})

    @classmethod
    def from_file(cls, filename: str) -> 'Config':
        if filename.endswith('.json'):
            return cls.from_json(filename)
        else:
            return cls.from_ini(filename)
