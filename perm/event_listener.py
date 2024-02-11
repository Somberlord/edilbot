from abc import ABC, abstractmethod

from perm.model.permanence import Permanence


class EventListener(ABC):

    @abstractmethod
    async def create_permanence(self, perm: Permanence):
        pass
