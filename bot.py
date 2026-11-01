import telebot, os
from telebot import types
from threading import Thread
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN", "9252155626:AAH2m-KSnGCWW4PE5uU1M1T1p7MeyZCfVMK4")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Sh4d0w_0x SUPER BOT ONLINE 24/7"

@bot.message_handler(commands=['start','help','menu'])
def start(m):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📁 Ajiye File", callback_data="file"),
        types.InlineKeyboardButton("🤖 AI Chat", callback_data="ai"),
        types.InlineKeyboardButton("⬇️ Download", callback_data="dl"),
        types.InlineKeyboardButton("ℹ️ Info", callback_data="info")
    )
    bot.send_message(m.chat.id, "🔥 **Sh4d0w_0x SUPER BOT** 🔥\n\nBarka da zuwa!\n1. Tura hoto/video zan ajiye\n2. Tura rubutu zan yi hira\n3. Tura link TikTok/YouTube zan sauke\n\nZabi ko tura abu yanzu!", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def cb(call):
    if call.data=="file": bot.send_message(call.message.chat.id, "📁 Tura min hoto/video/document yanzu!")
    elif call.data=="ai": bot.send_message(call.message.chat.id, "🤖 Ina jinka! Tambaya kowace ce!")
    elif call.data=="dl": bot.send_message(call.message.chat.id, "⬇️ Tura link na TikTok/YouTube/Instagram!")
    else: bot.send_message(call.message.chat.id, "👑 Sh4d0w_0x v2.0 - ONLINE 24/7")

@bot.message_handler(content_types=['photo','video','document','audio','voice'])
def files(m):
    bot.reply_to(m, "✅ Na ajiye file dinka! Idan ka sake bukata zan baka. Tura wani!")

@bot.message_handler(func=lambda m: True)
def allmsg(m):
    t=m.text.lower()
    if "tiktok.com" in t or "youtube" in t or "youtu.be" in t or "instagram.com" in t:
        bot.reply_to(m, f"⏳ Na karbi link: {m.text}\nZan sauke maka nan ba da jimawa!")
    elif "salam" in t or "hello" in t or "hi" in t:
        bot.reply_to(m, "Wa Alaikum Salam! 👋 Yaya kake?")
    elif "suna" in t or "waye kai" in t:
        bot.reply_to(m, "Ni Sh4d0w_0x Super Bot ne! 🔥")
    else:
        bot.reply_to(m, f"🤖 Na karba: {m.text}\nTura file ko link ko tambaya!")

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
def run_bot():
    bot.infinity_polling()
if __name__ == "__main__":
    Thread(target=run_flask).start()
    run_bot()
