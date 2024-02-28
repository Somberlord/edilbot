import json
import aiohttp

from perm.model.permanence import Permanence


class WordpressService:
    def __init__(self, bot):
        self.bot = bot
        wp_config = bot.config.wordpress_config
        self.wp_endpoint = f"{wp_config['BaseUrl']}/wp-json/tribe/events/v1/events"
        self.wp_auth = aiohttp.BasicAuth(login=wp_config['Login'], password=wp_config['AppPassword'])

    async def create_event(self, perm: Permanence):
        data = {
            "title": perm.title,
            "start_date": perm.start_date.strftime("%y-%m-%d %H:%M"),
            "end_date": perm.end_date.strftime("%y-%m-%d %H:%M"),
            "timezone": "Europe/Paris",
            "excerpt": perm.description,
            "description": perm.description,
        }
        async with aiohttp.ClientSession(auth=self.wp_auth) as session:
            async with session.post(self.wp_endpoint, data=data) as response:
                print("Status:", response.status)
                html = await response.text()
                data = json.loads(html)
                print(json.dumps(data, indent=2))
                # id should be saved to be able to delete / edit event
