from perm.event_listener import EventListener
from perm.model.permanence import Permanence
from perm.utils.permdateparser import PermDateParser


class WordpressEventListener(EventListener):

    def __init__(self, bot):
        self.bot = bot

    async def create_permanence(self, perm: Permanence):
        self.bot.logger.info("create permanence in wordpress")
        pdp = PermDateParser()
        date = pdp.get_date(perm.datestr, perm.startstr)
        print(date)
        print(date.period)
        print(date.date_obj)
