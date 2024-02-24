import dateparser.date
import re
from dateparser.date import DateDataParser


class InvalidTimeError(Exception):
    pass


class InvalidDateError(Exception):
    pass


class PermDateParser:
    def __init__(self):
        self.ddp = DateDataParser(languages=['fr', 'en'], try_previous_locales=True, region='FR',
                                  settings={'DATE_ORDER': 'DMY',
                                            'PREFER_LOCALE_DATE_ORDER': True,
                                            'TIMEZONE': 'Europe/Paris',
                                            'PREFER_DATES_FROM': 'future',
                                            'REQUIRE_PARTS': ['day'],
                                            'DEFAULT_LANGUAGES': ['fr']})

    @staticmethod
    def get_time(timestr) -> str:
        p = re.compile('(?P<hour>[0-2]?[0-9])[:h]?(?P<min>[0-5][0-9])?')
        m = p.search(timestr)
        if m is None:
            raise InvalidTimeError
        parsable_timestr = f"{m.group('hour')}:{m.group('min') or '00'}"
        return parsable_timestr

    def get_date(self, datestr: str, timestr: str) -> dateparser.date.DateData:
        parsable_timestr = PermDateParser.get_time(timestr)
        complete_date_str = f"{datestr} {parsable_timestr}"
        print(complete_date_str)
        data = self.ddp.get_date_data(complete_date_str)
        if data.date_obj is None:
            raise InvalidDateError
        return data
