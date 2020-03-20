import os
import telebot
import random
from telebot.types import Message

API_TOKEN = "1036931187:AAEgRa7nOS3nAsodpE-RGOKBZLRC-3_rasI"
#TOKEN = "1036931187:AAEgRa7nOS3nAsodpE-RGOKBZLRC-3_rasI"
#TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)
CHAT_ID = 250283754
SMILES = ['👍', '👌', '😊', '😂', '😘', '❤️', '😍', '😁', '☺️', '😔', '😄', '😭']

bot.send_message(CHAT_ID, "starting server... " + random.choice(SMILES))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "данная команда пока в разработке...")


@bot.message_handler(func=lambda m: True)
def upper(message: Message):
    bot.send_message(CHAT_ID, "мое настроение " + random.choice(SMILES))
    # print(message.from_user)
    # bot.reply_to(message, message.text.upper())
    # tb.send_sticker(message.chat_id)


bot.polling()
