import os
import threading
from flask import Flask
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Sh4d0w_0x is ONLINE 24/7!"

@bot.message_handler(commands=['start', 'help', 'menu'])
def handle_start(message):
    bot.reply_to(message, "🔥 Sh4d0w_0x is ONLINE 24/7!\n\nRubuta /help don taimako")

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    bot.reply_to(message, f"Ya karbi: {message.text}")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
