from telebot import TeleBot

from config.settings import settings


def init_bot(token):
    bot = TeleBot(token)
    return bot


bot = init_bot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['read'])
def send_welcome(message):
    with open("./media/file.txt", "r") as file:
        bot.reply_to(message, file.read())


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.infinity_polling()