from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 31072423))
        self.API_HASH = getenv("367b806c41b0899caa0b9958438583fe")

        self.BOT_TOKEN = getenv("8704729646:AAFavC9VpyXhnPdECoWDinXjEHqXzGFgrJ0")
        self.MONGO_URL = getenv("mongodb+srv://s46091175_db_user:aOCweoOGDbrzYM6R@cluster0.te58blz.mongodb.net")

        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = int(getenv("OWNER_ID", 8272317035))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION",1BVtsOHUBu5T1V45RvohJ5dwIZ0KsVkIgHWGKKHXebpa1AZZbmONT-Lif5na7XCy1uvtjHiofIrC3lKGZmziKDSAuzx9Kx8pzB9G5GV1RNmOPjn8BaWsrnBvKrHgziRH9JC7kmZZvvV9ZL9n1Jaw8QnQv0KP5JdXnWONUOeCLgHf7C4KVZ9UIrNV9w_K_ElgvayEeU6y2OoHGVrTpwwlWMiQBm9wb-7KZZNhe9CWLPzJR00gZ2buFoNQ6CIM3QHsocLcNDeq9sniYMHyfbO3DJZ5QGhvAIAI7bs7ZkGJt9FzcfwjP0w1DSoXNz9AVAnuhIrMt3BpcQ1deoS55zFhM74u2bSjgOAk=)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/LUFFY_COMUNITY")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LUFFY_COMUNITY")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
