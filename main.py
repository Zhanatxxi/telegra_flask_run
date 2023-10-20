import threading

from api import app
from apps.bot_telegram.bot_run import bot


def run_bot_and_flask():
    t = threading.Thread(target=bot.infinity_polling, daemon=True)
    t.start()
    app.run()


if __name__ == '__main__':
    run_bot_and_flask()