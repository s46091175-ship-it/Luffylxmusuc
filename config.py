from os import getenv

class Config:
    def __init__(self):
        self.API_ID = 31072423
        self.API_HASH = "367b806c41b0899caa0b9958438583fe"

        self.BOT_TOKEN = "8704729646:AAFavC9VpyXhnPdECoWDinXjEHqXzGFgrJ0"
        self.MONGO_URL = "mongodb+srv://s46091175_db_user:aOCweoOGDbrzYM6R@cluster0.te58blz.mongodb.net"

        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = 8272317035

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = "1BVtsOHUBu5T1V45RvohJ5dwIZ0KsVkIgHWGKKHXebpa1AZZbmONT-Lif5na7XCy1uvtjHiofIrC3lKGZmziKDSAuzx9Kx8pzB9G5GV1RNmOPjn8BaWsrnBvKrHgziRH9JC7kmZZvvV9ZL9n1Jaw8QnQv0KP5JdXnWONUOeCLgHf7C4KVZ9UIrNV9w_K_ElgvayEeU6y2OoHGVrTpwwlWMiQBm9wb-7KZZNhe9CWLPzJR00gZ2buFoNQ6CIM3QHsocLcNDeq9sniYMHyfbO3DJZ5QGhvAIAI7bs7ZkGJt9FzcfwjP0w1DSoXNz9AVAnuhIrMt3BpcQ1deoS55zFhM74u2bSjgOAk="
        self.SESSION2 = None
        self.SESSION3 = None

        self.SUPPORT_CHANNEL = "https://t.me/LUFFY_COMUNITY"
        self.SUPPORT_CHAT = "https://t.me/LUFFY_COMUNITY"

        self.AUTO_LEAVE = False
        self.AUTO_END = False
        self.THUMB_GEN = True
        self.VIDEO_PLAY = True

        self.LANG_CODE = "en"

        self.COOKIES_URL = []
        self.DEFAULT_THUMB = "https://te.legra.ph/file/3e40a408286d4eda24191.jpg"
        self.PING_IMG = "https://files.catbox.moe/haagg2.png"
        self.START_IMG = "https://files.catbox.moe/zvziwk.jpg"

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
