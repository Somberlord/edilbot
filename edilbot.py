from typing import Any

import discord
from config.botconfig import Config
from perm.perm import Permanence


class EdilBot(discord.Bot):
    # Init bot, load config
    def __init__(self, *args, **options):
        super().__init__(*args, **options)
        self.config = Config()

    # Add Cogs, run
    def run(self, *args: Any, **kwargs: Any) -> None:
        self.add_cog(Permanence(self, self.config.permanence_config))
        super().run(*args, **kwargs, token=self.config.client_secret)

    def get_config(self) -> Config:
        return self.config


def main():
    bot = EdilBot()
    bot.run()


if __name__ == "__main__":
    main()
