import pytest
from db.event_json_db import EventJsonDB

BASIC_CONTENT = '{"events":[{"name":"event1"},{"name":"event2"}]}'


def test_db_load_empty(tmp_path):
    p = tmp_path / 'emptydb'
    p.write_text("{}")
    db = EventJsonDB(str(p))
    db.load_from_disk()
    assert isinstance(db.data, dict)
    assert len(db.data) == 0


def test_db_load_basic(tmp_path):
    p = tmp_path / 'basicdb'
    p.write_text(BASIC_CONTENT)
    db = EventJsonDB(str(p))
    db.load_from_disk()
    assert isinstance(db.data, dict)
    assert len(db.data) == 1
    event_list = db.data['events']
    assert isinstance(event_list, list)
    assert len(event_list) == 2
    assert event_list[0] == {'name': 'event1'}
    assert event_list[1] == {'name': 'event2'}
