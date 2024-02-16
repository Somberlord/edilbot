import discord

from perm.event_listener import EventListener
from perm.model.permanence import Permanence


class WordpressEventListener(EventListener):

    def __init__(self, bot):
        self.bot = bot

    async def create_permanence(self, perm: Permanence):
        self.bot.logger.info("create permanence in wordpress")
