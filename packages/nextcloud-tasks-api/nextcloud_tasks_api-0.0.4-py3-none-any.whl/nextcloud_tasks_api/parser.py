import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
from .error import XmlError
from typing import Optional, Iterator, Generator, Tuple


class DavParser:
    """DAV XML request content and response payload parsing."""

    @classmethod
    def _iterparse(cls, content: Generator[bytes, None, None]) -> Iterator[ET.Element]:
        parser: ET.XMLPullParser = ET.XMLPullParser(("end",))
        try:
            for chunk in content:
                try:
                    parser.feed(chunk)
                    for event, elem in parser.read_events():
                        if event == "end":
                            yield elem
                except Exception as e:
                    content.close()
                    raise XmlError(f"Cannot parse XML response: {str(e)}") from None
        finally:
            parser.close()

    @classmethod
    def _parse_propstat(cls, elements: Iterator[ET.Element], code: int = 200) -> Iterator[Tuple[str, ET.Element]]:
        for response in elements:
            if response.tag == "{DAV:}response":
                href: Optional[ET.Element] = response.find("{DAV:}href")
                if href is None or not href.text:
                    continue
                for propstat in response.findall("{DAV:}propstat"):
                    status: Optional[ET.Element] = propstat.find("{DAV:}status")
                    if status is None or status.text is None or f" {code} " not in status.text:
                        continue
                    yield href.text, propstat

    @classmethod
    def parse_propstat_for_status(cls, content: Generator[bytes, None, None]) -> Iterator[str]:
        """Response hrefs with success statuscode."""

        for href, _ in cls._parse_propstat(cls._iterparse(content), code=200):
            yield href

    @classmethod
    def parse_list_for_calendars(cls, content: Generator[bytes, None, None]) -> Iterator[Tuple[str, Optional[str]]]:
        """Calendar/list hrefs and displaynames."""

        for href, propstat in cls._parse_propstat(cls._iterparse(content)):
            if propstat.find("./{DAV:}prop/{DAV:}resourcetype/{urn:ietf:params:xml:ns:caldav}calendar") is None:
                continue

            name: Optional[ET.Element] = propstat.find("./{DAV:}prop/{DAV:}displayname")
            yield href, name.text if name is not None and name.text else None

    @classmethod
    def parse_get_for_calendar(cls, content: Generator[bytes, None, None]) -> Iterator[Tuple[str, Optional[str], str]]:
        """Task hrefs, etags, and data."""

        for href, propstat in cls._parse_propstat(cls._iterparse(content)):
            getetag: Optional[ET.Element] = propstat.find("./{DAV:}prop/{DAV:}getetag")

            getcontenttype: Optional[ET.Element] = propstat.find("./{DAV:}prop/{DAV:}getcontenttype")
            if getcontenttype is None or getcontenttype.text != "text/calendar; charset=utf-8; component=vtodo":
                continue

            calendar: Optional[ET.Element] = propstat.find("./{DAV:}prop/{urn:ietf:params:xml:ns:caldav}calendar-data")
            if calendar is None or not calendar.text:
                continue

            yield href, getetag.text if getetag is not None and getetag.text else None, calendar.text

    @classmethod
    def get_propfind_calendars(cls) -> bytes:
        """Request calendar/list properties."""

        # language=XML
        return b"""<x0:propfind xmlns:x0="DAV:">
                     <x0:prop>
                       <x0:resourcetype/><x0:displayname/>
                     </x0:prop>
                   </x0:propfind>"""

    @classmethod
    def get_propfind_calendar(cls) -> bytes:
        """Request task properties."""

        # language=XML
        return b"""<x0:propfind xmlns:x0="DAV:" xmlns:x1="urn:ietf:params:xml:ns:caldav">
                     <x0:prop>
                       <x0:getcontenttype/><x0:getetag/><x1:calendar-data/>
                     </x0:prop>
                   </x0:propfind>"""

    @classmethod
    def get_report_calendar(cls, completed_filter: Optional[bool]) -> bytes:
        """Request tasks of a calendar/list."""

        if completed_filter is None:
            task_filter: bytes = b''
        elif completed_filter:
            task_filter = b'<x1:prop-filter name="completed"><x1:is-defined/></x1:prop-filter>'
        else:
            task_filter = b'<x1:prop-filter name="completed"><x1:is-not-defined/></x1:prop-filter>'

        return b"""<x1:calendar-query xmlns:x0="DAV:" xmlns:x1="urn:ietf:params:xml:ns:caldav">
                     <x0:prop>
                       <x0:getcontenttype/><x0:getetag/><x1:calendar-data/>
                     </x0:prop>
                     <x1:filter>
                       <x1:comp-filter name="VCALENDAR">
                         <x1:comp-filter name="VTODO">
                           %b
                         </x1:comp-filter>
                       </x1:comp-filter>
                     </x1:filter>
                   </x1:calendar-query>""" % task_filter

    @classmethod
    def get_mkcol_calendar(cls, name: str) -> bytes:
        """Request creating a calendar/list."""

        return b"""<x0:mkcol xmlns:x0="DAV:" xmlns:x1="urn:ietf:params:xml:ns:caldav">
                     <x0:set><x0:prop>
                       <x0:displayname>%b</x0:displayname>
                       <x0:resourcetype>
                          <x0:collection/><x1:calendar/>
                       </x0:resourcetype>
                       <x1:supported-calendar-component-set>
                         <x1:comp name="VTODO"/>
                       </x1:supported-calendar-component-set>
                     </x0:prop></x0:set>
                   </x0:mkcol>""" % escape(name).encode("utf-8", errors="strict")

    @classmethod
    def get_property_update(cls, name: str) -> bytes:
        """Request a calendar/list update."""

        return b"""<x0:propertyupdate xmlns:x0="DAV:">
                     <x0:set><x0:prop>
                       <x0:displayname>%b</x0:displayname>
                     </x0:prop></x0:set>
                   </x0:propertyupdate>""" % escape(name).encode("utf-8", errors="strict")
