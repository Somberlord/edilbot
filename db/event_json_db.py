import json

from db.event_db import EventDB
from perm.model.permanence import Permanence, DATA_DISCORD, DATA_WP

EVENTS = 'events'


class EventJsonDB(EventDB):

    def __init__(self, filename):
        self.dbpath = filename
        self.data = dict()
        self.data[EVENTS] = []

    def __create_empty_db(self):
        with open(self.dbpath, mode='w') as f:
            f.write("{}")

    def load_from_disk(self):
        try:
            with open(self.dbpath, mode='r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.__create_empty_db()
            self.load_from_disk()

    def save_to_disk(self):
        with open(self.dbpath, mode='w') as f:
            json.dump(self.data, f)

    def event_index(self, criterion: str = None, value=None) -> (bool, int):
        for idx, event in enumerate(self.data[EVENTS]):
            event_data: dict = event.data
            if criterion in event_data.keys():
                if event_data[criterion] == value:
                    return True, idx
        return False, -1

    def find_event(self, perm: Permanence) -> (bool, int):
        perm_data = perm.data
        if DATA_DISCORD in perm_data.keys():
            found, idx = self.event_index(DATA_DISCORD, perm_data[DATA_DISCORD])
            if found:
                return True, idx
        if DATA_WP in perm_data.keys():
            found, idx = self.event_index(DATA_WP, perm_data[DATA_WP])
            if found:
                return True, idx
        return False, -1

    def save_event(self, perm: Permanence) -> None:
        found, idx = self.find_event(perm)
        if found:
            self.data[EVENTS].insert(idx, perm)
        else:
            self.data[EVENTS].append(perm)
        self.save_to_disk()

    def load_event(self, perm: Permanence) -> Permanence:
        pass
