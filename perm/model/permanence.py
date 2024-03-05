import json

from perm.utils.permdateparser import PermDateParser, InvalidTimeError, InvalidDateError

INVALID_DATE = 'invalid_date'
INVALID_START_TIME = 'invalid_start_time'
INVALID_END_TIME = 'invalid_end_time'
VALID_TIMES = 'valid_times'

DATA_DISCORD = 'discord'
DATA_WP = 'wordpress'


class Permanence:
    def __init__(self, title="", datestr="", startstr="", endstr="", description=""):
        self.title: str = title
        self.datestr: str = datestr
        self.startstr: str = startstr
        self.endstr: str = endstr
        self.description: str = description
        self.start_date = None
        self.end_date = None
        self.data = dict()

    def validate(self):
        try:
            dateparser = PermDateParser()
            self.start_date = dateparser.get_date(self.datestr, self.startstr).date_obj
        except InvalidDateError:
            return INVALID_DATE
        except InvalidTimeError:
            return INVALID_START_TIME
        try:
            self.end_date = dateparser.get_date(self.datestr, self.endstr).date_obj
        except InvalidTimeError:
            return INVALID_END_TIME
        return VALID_TIMES


class PermanenceJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, list):
            res = []
            for item in obj:
                res.append(self.default(item))
            return res
        elif isinstance(obj, Permanence):
            res_dict = {
                "title": obj.title,
                "datestr": obj.datestr,
                "startstr": obj.startstr,
                "endstr": obj.endstr,
                "description": obj.description,
            }
            if len(obj.data) > 0:
                res_dict["data"] = obj.data
            return res_dict
        else:
            return super().default(obj)
