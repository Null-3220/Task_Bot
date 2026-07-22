import telebot
from config import TOKEN
from commands import start
from commands import add
from commands import remove
from commands import list

bot = telebot.TeleBot(TOKEN)

start.register(bot)
add.register(bot)
remove.register(bot)
list.register(bot)

bot.polling()