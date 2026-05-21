from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes,filters,)
#update = use for receiving data from user
# command handler uses for doing something after user send a command

token = "some token"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["start", ],["contact with akram",],"Akram's projects"]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Hi, click one of the options")
# help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("this bot is ready for helping you for the following commands")
# function for receiving message
async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "/start":
        await update.message.reply_text("hi I can help you for these commands\n")
        "searching for jobs in acbar site\n"
        "some thing\n"
    else:
        await update.message.reply_text("you write a wrong command")
# reply buttons

#update, telegram put every thing in update

#update.message the message that user send
#reply text what do you want to show after receiving the message from user
# async uses for responding the  answer for multiple user
app = ApplicationBuilder().token(token).build() #buil the bot and connecting to the token, main manager
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(MessageHandler(filters.TEXT & filters.COMMAND, message ))
print("bot is running...")
app.run_polling()
#polling ask repeatedly from the telegram that do you have message if there was robot and functions
# will respond

