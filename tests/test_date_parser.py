import pytest
from perm.utils.permdateparser import PermDateParser, InvalidTimeError, InvalidDateError


def test_get_time_simple() -> None:
    assert PermDateParser.get_time("14") == "14:00"
    assert PermDateParser.get_time("14h") == "14:00"
    assert PermDateParser.get_time("14h30") == "14:30"
    assert PermDateParser.get_time("1430") == "14:30"
    assert PermDateParser.get_time("14:30") == "14:30"


def test_get_time_error() -> None:
    with pytest.raises(InvalidTimeError):
        PermDateParser.get_time("text")


def test_get_date_simple() -> None:
    dateparser = PermDateParser()
    res = dateparser.get_date("14/02/2025", "14h")
    assert res.date_obj.day == 14
    assert res.date_obj.month == 2
    assert res.date_obj.year == 2025
    assert res.date_obj.hour == 14
    assert res.date_obj.minute == 0


def test_get_date_year() -> None:
    with pytest.raises(InvalidDateError):
        dateparser = PermDateParser()
        dateparser.get_date("mai 2025", "14h")
