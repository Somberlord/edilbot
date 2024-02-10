import configparser
CONFIG_FILE = "config/config.ini"


class Config:
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read(CONFIG_FILE)
        # Global configuration
        self.client_secret = parser['global']['DiscordAuthToken']
        # Permanence configuration
        self.permanence_config = parser['permanence']
