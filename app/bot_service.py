import os

from pymessenger import Bot

_bot: Bot = None


def get_bot() -> Bot:
    global _bot
    if _bot is None:
        access_token = os.getenv('ACCESS_TOKEN')
        _bot = Bot(access_token)
    return _bot


if __name__ == "__main__":
    print(get_bot())
