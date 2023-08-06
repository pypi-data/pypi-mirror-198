from typing import List, Tuple, Set, Optional, Iterator, ClassVar

from datetime import datetime, timezone
from time import time
from uuid import uuid4
import re


class ICal:
    """
    Simple datastructure on (key, parameter, value) tuples for vCalendar/vEvent/iCal payload.
    Only internally used by the optional Task objects, so not necessarily involved in general API usage.
    """

    _read_only_keys: ClassVar[Set[str]] = {'BEGIN', 'END'}

    def __init__(self, data: List[Tuple[str, str, str]]) -> None:
        self._data: List[Tuple[str, str, str]] = data  # key, parameter, value

    @property
    def data(self) -> List[Tuple[str, str, str]]:
        """Expose direct access to the underlying datastructure."""
        return self._data

    def _index(self, key: str, param: Optional[str] = None, value: Optional[str] = None) -> Optional[int]:
        key = key.upper()
        for i, kv in enumerate(self._data):
            if key == kv[0].upper():
                if param is not None and param != kv[1]:
                    continue
                elif value is not None and value != kv[2]:
                    continue
                else:
                    return i
        return None

    def find(self, key: str, param: Optional[str] = None) -> Optional[Tuple[str, str]]:
        """Find the first match as parameter/value for the given arguments, if any."""
        i: Optional[int] = self._index(key, param)
        return (self._data[i][1], self.unescape(self._data[i][2])) if i is not None else None

    def insert(self, key: str, param: str, value: str) -> None:
        """Insert a new VTODO section key/parameter/value. Duplicates are technically allowed but discouraged."""
        if key.upper() in self._read_only_keys:
            raise ValueError(f"Inserting ical '{key}' not allowed")
        i: Optional[int] = self._index("BEGIN", "", "VTODO")
        if i is None:
            raise KeyError("BEGIN:VTODO")
        self._data.insert(i + 1, (key, param, self.escape(value.rstrip())))

    def update(self, key: str, param: Optional[str], value: str) -> None:
        """Update the value of an already existing key/parameter, if any."""
        if key.upper() in self._read_only_keys:
            raise ValueError(f"Updating ical '{key}' not allowed")
        i: Optional[int] = self._index(key, param)
        if i is None:
            raise KeyError(key)
        self._data[i] = (key, param if param is not None else "", self.escape(value.rstrip()))

    def remove(self, key: str, param: Optional[str] = None, value: Optional[str] = None) -> None:
        """Remove all instances of the given key/parameter/value."""
        if key.upper() in self._read_only_keys:
            raise ValueError(f"Removing ical '{key}' not allowed")
        while True:
            i: Optional[int] = self._index(key, param, value)
            if i is None:
                break
            del self._data[i]

    def find_value(self, key: str) -> Optional[str]:
        """Find the first value of the given key, ignoring parameters."""
        value: Optional[Tuple[str, str]] = self.find(key)
        return value[1] if value is not None else None

    def upsert_value(self, key: str, value: Optional[str]) -> None:
        """Convenience helper that silently ignores/replaces parameters."""
        if value is None:
            self.remove(key)
            return
        try:
            self.update(key, None, value)
        except KeyError:
            self.insert(key, "", value)

    @classmethod
    def escape(cls, s: str) -> str:
        """Escaping for iCal values."""
        s = s.replace("\\", "\\\\")
        s = s.replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")
        if re.search(r'[\x00-\x1f\x7e-\x7f]', s) is not None:
            raise ValueError("ical: Invalid character")
        return s

    @classmethod
    def unescape(cls, s: str) -> str:
        """Decoding of iCal values."""
        def repl(match: re.Match) -> str:
            c = match.group(1)
            return "\n" if c == "n" else c
        return re.sub(r'\\([\\;,n])', repl, s)


class ICalParser:
    """
    Minimal parser and factory for iCal datastructures from raw API payload.
    https://datatracker.ietf.org/doc/html/rfc5545#section-3.1
    """

    @classmethod
    def from_string(cls, data: str) -> ICal:
        """Parse API payload into iCal datastructure."""
        return ICal(cls.parse(data))

    @classmethod
    def to_string(cls, data: ICal) -> str:
        """Format as serialized iCal payload."""
        return cls.serialize(data.data)

    @classmethod
    def create(cls) -> ICal:
        """Give a new iCal datastructure as default skeleton."""
        uid: str = str(uuid4())
        ts: str = cls.from_timestamp(int(time()))
        return ICal([
            ("BEGIN", "", "VCALENDAR"),
            ("VERSION", "", "2.0"),
            ("PRODID", "", "-//hackitu.de/Nextcloud Tasks API Client"),
            ("BEGIN", "", "VTODO"),
            ("UID", "", uid),
            ("CREATED", "", ts),
            ("LAST-MODIFIED", "", ts),
            ("DTSTAMP", "", ts),
            ("SUMMARY", "", ""),
            ("END", "", "VTODO"),
            ("END", "", "VCALENDAR"),
        ])

    @classmethod
    def parse(cls, data: str) -> List[Tuple[str, str, str]]:
        """Generic iCal tuple parsing, without unescaping actual values."""
        pattern: re.Pattern = re.compile(
            r'^(?P<key>[A-Za-z0-9-]+)'
            r'(;(?P<tzid>TZID=("[^"]*"|[^";:,]*)(,("[^"]*"|[^";:,]*))*))?'
            r'(?P<param>(;[A-Za-z0-9-]+=("[^"]*"|[^";:,]*)(,("[^"]*"|[^";:,]*))*)*)'
            r':(?P<value>.*)'
        )
        ical: List[Tuple[str, str, str]] = []

        for line in data.splitlines(keepends=False):
            if line.startswith(' '):  # continuation
                if not len(ical):
                    raise ValueError("Cannot parse ical: continuation start")
                ical[-1] = ical[-1][0], ical[-1][1], ical[-1][2] + line[1:]  # unfolding
            else:
                match: Optional[re.Match] = pattern.match(line)
                if match is None:
                    raise ValueError(f"Cannot parse ical: '{line}'")
                ical.append((match.group('key'), match.group('param') or '', match.group('value') or ''))

        return ical

    @classmethod
    def serialize(cls, data: List[Tuple[str, str, str]]) -> str:
        """Generic key/parameter/value tuple formatting into iCal payload, without escaping actual values."""
        def blen(s: str, maxwidth: int) -> int:  # don't split in-between utf-8
            for slen in range(min(maxwidth, len(s)), 0, -1):
                if len(s[:slen].encode("utf-8", errors="strict")) <= maxwidth:
                    return slen
            raise ValueError(f"ical: Cannot find substring of length {maxwidth}")  # excluding 0

        def fold(s: str) -> Iterator[str]:  # excluding line break
            prefix: str = ''
            while len(s):
                pop_len: int = blen(s, 75)
                line, s = s[:pop_len], s[pop_len:]
                yield prefix + line
                if len(s):
                    s = ' ' + s

        lines: List[str] = []
        for k, p, v in data:
            if re.fullmatch(r'[A-Za-z0-9-]+', k) is None:
                raise ValueError(f"ical: Invalid key '{k}'")
            if p and re.fullmatch(r'(;[A-Za-z0-9-] += ("[^"] * "|[^";:,] * )(, ("[^"] * "|[^";:, ] *)) * )*', p) is None:
                raise ValueError(f"ical: Invalid parameter '{p}'")
            lines.extend(fold(f"{k}{';' + p if p else ''}:{v}"))

        return "\r\n".join(lines) + "\r\n"

    @classmethod
    def parse_timestamp(cls, ts_str: str) -> int:
        """Parse datetime into unix timestamp, assuming UTC."""
        try:
            if isinstance(ts_str, tuple):
                for item in ts_str:
                    # Skip empty or A=B values
                    if not len(item) or re.match("^.*=.*", item):
                        continue
                    else:
                        ts_str = item
                        break
            if not isinstance(ts_str, str):
                raise ValueError("ical: invalid type for ts_str:'{}', content:'{}'".format(type(ts_str),ts_str))
            if len(ts_str) == 8:
                ts_str += "T000000"
            return int(datetime.strptime(ts_str.rstrip('Z'), "%Y%m%dT%H%M%S").replace(tzinfo=timezone.utc).timestamp())
        except (ValueError, UnicodeError, OSError, OverflowError) as e:
            raise ValueError(f"ical: Cannot parse timestamp '{ts_str}': {repr(e)}") from None

    @classmethod
    def from_timestamp(cls, ts_int: int) -> str:
        """Format unix timestamp as datetime, in UTC."""
        return datetime.fromtimestamp(ts_int, timezone.utc).strftime("%Y%m%dT%H%M%SZ")
