import sys
from typing import Any

import discord
import logging
from config.botconfig import Config
from perm.permanencecog import PermanenceCog
from perm.wordpress.wordpress_event_listener import WordpressEventListener


class EdilBot(discord.Bot):
    # Init bot, load config
    def __init__(self, *args, **options):
        super().__init__(*args, **options)
        self.config = Config()
        # Set up pycord logging
        discord_logger = logging.getLogger('discord')
        discord_logger.setLevel(self.config.discord_log_level)
        discord_handler = logging.FileHandler(filename=self.config.discord_log_filename,
                                              encoding='utf-8', mode='w')
        discord_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        discord_logger.addHandler(discord_handler)

        # Set up edilbot logger
        edilbot_logger = logging.getLogger('edilbot')
        edilbot_logger.setLevel(self.config.edilbot_log_level)
        if self.config.edilbot_log_filename == self.config.discord_log_filename:
            edilbot_handler = discord_handler
        else:
            edilbot_handler = logging.FileHandler(filename=self.config.edilbot_log_filename,
                                                  encoding='utf-8', mode='w')
            edilbot_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        edilbot_logger.addHandler(edilbot_handler)
        edilbot_logger.addHandler(logging.StreamHandler(sys.stdout))
        self.logger = edilbot_logger

    # Add Cogs, run
    def run(self, *args: Any, **kwargs: Any) -> None:
        cog = PermanenceCog(self, self.config.permanence_config)
        wp_listener = WordpressEventListener(self)
        cog.add_event_listener(wp_listener)
        self.add_cog(cog)
        super().run(*args, **kwargs, token=self.config.client_secret)

    def get_config(self) -> Config:
        return self.config


def main():
    bot = EdilBot()
    bot.run()


if __name__ == "__main__":
    main()
