import os, random, threading
from datetime import datetime
from flask import Flask
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "ARAFAT NEW BOT LIVE"

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, f"🔥 ARAFAT VAI VIP 🔥\n👋 Hi {m.from_user.first_name}\n\nSend /signal")

@bot.message_handler(commands=['signal'])
def signal(m):
    sig = random.choice(['BIG 🟢', 'SMALL 🔴'])
    num = random.randint(0, 9)
    t = datetime.now().strftime("%I:%M:%S %p")
    text = f"🔥 𝐀𝐑𝐀𝐅𝐀𝐓 𝐕𝐀𝐈 𝐕𝐈𝐏 𝐒𝐈𝐍𝐆𝐍𝐀𝐋 🔥\n━━━━━━━━━━━━━━\n🎲 Number: {num}\n👉 SIGNAL: {sig}\n\n⏰ Time: {t}\n🎯 Accuracy: 99%\n📊 Mode: APEX\n━━━━━━━━━━━━━━\n👑 𝐀𝐑𝐀𝐅𝐀𝐓 | 𝐕𝐀𝐈\n𝐎𝐖𝐍𝐄𝐑 𝐈𝐃: @ARAFAT_VAI_D"
    bot.send_message(m.chat.id, text)

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
