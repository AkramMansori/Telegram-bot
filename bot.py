
import requests
from bs4 import BeautifulSoup
import asyncio
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
from dotenv import load_dotenv
import os
load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")

# ---------------- GET ALL JOBS ---------------- #

def get_jobs():

    jobs = []
    seen = set()

    page = 1

    while True:

        url = f"https://www.acbar.org/jobs?page={page}"

        try:

            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.content, "html.parser")

            rows = soup.find_all("tr")

            # stop if page has no jobs
            if not rows:
                break

            found_job = False

            for row in rows:

                a = row.find("a")

                if a:

                    title = a.get_text(strip=True)
                    link = a.get("href")

                    if title and link:

                        found_job = True

                        if link.startswith("/"):
                            link = "https://www.acbar.org" + link

                        # remove duplicates
                        if link not in seen:

                            seen.add(link)

                            jobs.append((title, link))

            # stop if no valid jobs found
            if not found_job:
                break

            print(f"Page {page} scraped")

            page += 1

        except Exception as e:

            print("Error:", e)
            break

    return jobs


# ---------------- START ---------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton(
                "📋 List Jobs",
                callback_data="jobs"
            )
        ],

        [
            InlineKeyboardButton(
                "📱 MY WhatsApp",
                url="https://wa.me/+93767944689"
            )
        ],

        [
            InlineKeyboardButton(
                "✈️ My Telegram ",
                url="https://t.me/َAkramBromand"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome 👋\nChoose an option:",
        reply_markup=reply_markup
    )


# ---------------- BUTTONS ---------------- #

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "jobs":

        await query.message.reply_text(
            "⏳ Getting all jobs..."
        )

        jobs = get_jobs()

        if not jobs:

            await query.message.reply_text(
                "No jobs found."
            )
            return

        await query.message.reply_text(
            f"✅ {len(jobs)} jobs found."
        )

        # send jobs slowly to avoid telegram flood limit
        for title, link in jobs:

            text = f"📌 {title}\n🔗 {link}"

            await query.message.reply_text(text)

            await asyncio.sleep(0.5)


# ---------------- MAIN ---------------- #

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        CallbackQueryHandler(buttons)
    )

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
# ---------------- GET JOBS ---------------- #

def get_jobs():

    jobs = []

    # change range as you want
    for page in range(1, 20):

        url = f"https://www.acbar.org/jobs?page={page}"

        try:

            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.content, "html.parser")

            for row in soup.find_all("tr"):

                a = row.find("a")

                if a:

                    title = a.get_text(strip=True)
                    link = a.get("href")

                    if title and link:

                        if link.startswith("/"):
                            link = "https://www.acbar.org" + link

                        jobs.append((title, link))

        except Exception as e:
            print("Error:", e)

    return jobs


# ---------------- START ---------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton(
                "📋 List Jobs",
                callback_data="jobs"
            )
        ],

        [
            InlineKeyboardButton(
                "📱 WhatsApp",
                url="https://wa.me/+93767944689"
            )
        ],

        [
            InlineKeyboardButton(
                "✈️ Telegram",
                url="https://t.me/AkramBromand001"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome 👋\nChoose an option:",
        reply_markup=reply_markup
    )


# ---------------- BUTTON HANDLER ---------------- #

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "jobs":

        await query.message.reply_text(
            "⏳ Getting jobs..."
        )

        jobs = get_jobs()

        if not jobs:

            await query.message.reply_text(
                "No jobs found."
            )

            return

        # send jobs

        for title, link in jobs[:50]:

            text = f"📌 {title}\n🔗 {link}"

            await query.message.reply_text(text)


# ---------------- MAIN ---------------- #

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        CallbackQueryHandler(buttons)
    )

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()






