import json

from db.event_db import EventDB
from perm.model.permanence import Permanence


class EventJsonDB(EventDB):

    def __init__(self, filename):
        self.dbpath = filename
        self.data = dict()
        self.data['events'] = []

    def load_from_disk(self):
        with open(self.dbpath) as f:
            self.data = json.load(f)

    def save_event(self, perm: Permanence) -> None:
        pass

    def load_event(self, perm: Permanence) -> Permanence:
        pass

