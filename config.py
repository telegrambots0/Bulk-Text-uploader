import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7073327110:AAGFGVPzzqquAQNMBXACtyZRv5UuVvOIGgg")
    
    API_ID = int(os.environ.get("API_ID", "25263708"))
    API_HASH = os.environ.get("API_HASH", "9bde48b267ce65a576b478c0ff8c7bbb")
    AUTH_USERS = os.environ.get("AUTH_USERS","6955269919")
    
