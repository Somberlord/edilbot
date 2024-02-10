# TODO read config file
AUTH_FILE = "config/AUTH_TOKEN"


class Config:
    def __init__(self):
        with open(AUTH_FILE) as f:
            self.client_secret = f.read().strip()
        self.perm_channel = 1203803021096783953
