import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6662229253:AAFfxR0lHLdvfJsaAbM5FJVYpxv19tfj-fE")
    
    API_ID = int(os.environ.get("API_ID", "29768900"))
    API_HASH = os.environ.get("API_HASH", "6a56e5c2383dc7b85210febe60b9f229")
    AUTH_USERS = os.environ.get("AUTH_USERS","5986670447")
    
