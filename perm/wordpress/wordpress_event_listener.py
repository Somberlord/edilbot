from perm.event_listener import EventListener
from perm.model.permanence import Permanence
from perm.wordpress.wordpress_service import WordpressService


class WordpressEventListener(EventListener):

    def __init__(self, bot):
        self.bot = bot
        self.wp_service = WordpressService(bot)

    async def create_permanence(self, perm: Permanence):
        self.bot.logger.info("create permanence in wordpress")
        await self.wp_service.create_event(perm)
