import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from keep_alive import keep_alive

# Start dummy Flask server to keep alive on Render
keep_alive()

# Your Telegram bot token (⚠️ DO NOT SHARE THIS IN PUBLIC)
TOKEN = "8038937835:AAH6Mg7B9GvAHtYHS0Vyez5n3r5qgIwY5Kw"

# Your file list
file_list = """
This is all the available things. Copy and paste in the chat box:

words in context
text structure and purpose
cross text connection answers
form, structure, sense annotation
central ideas and details
command of evidence textual
command of evidence quantitative
command of evidence quantitative practice
inference
inference answers
punctuation
punctuation (no answer)
subject-verb agreement
verb tenses
finite and non finite
pronouns
modifiers
run ons & fragments
transitions
transition practice
transition practice & explanation
rhetorical synthesis practice
rhetorical synthesis practice & explanation
test 15
test 15 marked
test 16
test 16 marked
test 17
test 17 marked
test 18
test 18 marked
vocabulary (the eloquent ones)
"""

# Replace with real file paths if you have them
file_lookup = {
    "words in context": "files/words in context.pdf",
    "text structure and purpose": "files/text structure and purpose.pdf",
    # Add all other mappings...
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome!\n" + file_list)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()

    if text in file_lookup:
        try:
            with open(file_lookup[text], 'rb') as doc:
                await update.message.reply_document(document=doc)
        except:
            await update.message.reply_text("⚠️ Error sending file.")
    else:
        await update.message.reply_text("❌ File not found.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
