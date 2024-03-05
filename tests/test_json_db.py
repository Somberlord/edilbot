import json
from json import JSONDecodeError

import pytest
from db.event_json_db import EventJsonDB, EVENTS
from perm.model.permanence import Permanence

BASIC_CONTENT = '{"events":[{"name":"event1"},{"name":"event2"}]}'
BASIC_DATA = {"events": [{"name": "event1"}, {"name": "event2"}]}
BASIC_PERM = Permanence(title="mytitle", datestr="10/05/2025", startstr="14h",
                        endstr="18h", description="mydescription")
BASIC_PERM.validate()


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


def test_db_load_nofile(tmp_path):
    p = tmp_path / 'nodb'
    db = EventJsonDB(str(p))
    db.load_from_disk()
    assert isinstance(db.data, dict)
    assert len(db.data) == 0


def test_db_load_nojson(tmp_path):
    p = tmp_path / 'nojson'
    p.write_text("not json")
    db = EventJsonDB(str(p))
    with pytest.raises(JSONDecodeError):
        db.load_from_disk()


def test_save_to_disk(tmp_path):
    p = tmp_path / 'saveddb'
    db = EventJsonDB(str(p))
    db.data = BASIC_DATA
    db.save_to_disk()
    with open(str(p)) as f:
        loaded_data = json.load(f)
        assert loaded_data == BASIC_DATA


def test_save_perm(tmp_path):
    p = tmp_path / 'saveddb'
    db = EventJsonDB(str(p))
    db.data = BASIC_DATA
    db.save_event(BASIC_PERM)
    # with open(str(p)) as f:
    #     print(f.read())
    # db2 = EventJsonDB(str(p))
    # db2.load_from_disk()
    # print(db2.data[EVENTS][0])
    # assert db2.data[EVENTS][0] == BASIC_PERM
