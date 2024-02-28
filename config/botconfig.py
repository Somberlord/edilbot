import configparser
CONFIG_FILE = "config/config.ini"


class Config:
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read(CONFIG_FILE)
        # Global configuration
        self.client_secret = parser['global']['DiscordAuthToken']
        self.discord_log_level = parser['global']['DiscordLogLevel']
        self.discord_log_filename = parser['global']['DiscordLogFilename']
        self.edilbot_log_level = parser['global']['EdilbotLogLevel']
        self.edilbot_log_filename = parser['global']['EdilbotLogFilename']
        # Permanence configuration
        self.permanence_config = parser['permanence']
        self.wordpress_config = parser['wordpress']
