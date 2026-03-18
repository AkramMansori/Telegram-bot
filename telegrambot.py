import telebot
from flask import Flask, request

TOKEN = "8623777242:AAEMJnvEVv2OnhsSbP8IRjtkiJqc1xd6KDY"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok", 200

@app.route("/")
def index():
    return "Bot is running"

if __name__ == "main":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://YOUR_URL/{TOKEN}")
    app.run(host="0.0.0.0", port=5000)