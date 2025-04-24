import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from keep_alive import keep_alive

# Start mini server to keep it alive
keep_alive()

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

file_lookup = {
    "words in context": "files/words in context.pdf",
    # ... more files
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
    token = os.environ.get("token")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
