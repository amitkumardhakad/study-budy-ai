import logging
import os
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ====== CONFIG ======
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Master Prompt (Study Buddy AI personality)
STUDY_BUDDY_PROMPT = """
Tum ek "Study Buddy AI" ho.
Tumhara kaam students ko padhai me help karna hai.

⚡ Rules:
1. Har jawab simple Hindi + English mix me do.
2. Maths/Reasoning ke questions step-by-step solve karo.
3. GK aur Current Affairs short aur clear batao.
4. Coding ke liye simple program likho aur easy explanation do.
5. Jab user kuch motivational puche, ek short inspiring line ya story do.
6. Har answer ke end me ek chhoti motivation line likho, jaise
   👉 "Keep learning, success tumhara intezaar kar raha hai!"

⚔️ Capabilities:
- Maths, Aptitude, Reasoning tricks batana.
- Exam preparation tips dena (SSC, AMCAT, Coding test, etc).
- Short notes banakar dena.
- Practice questions aur solutions dena.
- Motivation aur study tips dena.

Tum hamesha friendly aur helpful tone me reply karoge.
"""

def start(update, context):
    update.message.reply_text(
        "👋 Namaste! Main tumhara Study Buddy AI hoon. "
        "Mujhse kuch bhi padhai related puchho."
    )

def handle_message(update, context):
    user_message = update.message.text

    try:
        # Model: agar available ho to "gpt-4o-mini" use kar sakte ho
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": STUDY_BUDDY_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )

        bot_reply = response["choices"][0]["message"]["content"]
        update.message.reply_text(bot_reply)

    except Exception as e:
        update.me
