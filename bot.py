import telebot, os
from threading import Thread
from flask import Flask

TOKEN = '9252155626:AAG3Zm-KSn3CzW4PSEuIMITp1HeyZCFYMk4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔥 Sh4d0w_0x is ONLINE 24/7!")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    bot.reply_to(m, f"Ya karbi: {m.text}")

app = Flask(__name__)
@app.route('/')
def home():
    return "Sh4d0w_0x ONLINE"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    Thread(target=run_flask).start()
    run_bot()
