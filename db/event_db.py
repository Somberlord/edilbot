from abc import ABC, abstractmethod

from perm.model.permanence import Permanence


class EventDB(ABC):

    @abstractmethod
    def save_event(self, perm: Permanence) -> None:
        pass

    @abstractmethod
    def load_event(self, perm: Permanence) -> Permanence:
        pass
