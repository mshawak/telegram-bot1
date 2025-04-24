import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

# FILE LIST
file_lookup = {
    "words in context": "files/words in context.pdf",
    "text structure and purpose": "files/Text Structure And Purpose.pdf",
    "cross text connection answers": "files/Cross text connection answers.pdf",
    "form, structure, sense annotation": "files/Form, Structure, Sense Annotation.pdf",
    "central ideas and details": "files/Central ideas and details.pdf",
    "command of evidence textual": "files/Command of evidence textual.pdf",
    "command of evidence quantitative": "files/Command of evidence quantitative.pdf",
    "command of evidence quantitative practice": "files/Command of evidence quantitative practice.pdf",
    "inference": "files/Inference.pdf",
    "inference answers": "files/Inference answers.pdf",
    "punctuation": "files/Punctuation.pdf",
    "punctuation (no answer)": "files/Punctuation (No ANSWER).pdf",
    "subject-verb agreement": "files/Subject-Verb Agreement.pdf",
    "verb tenses": "files/Verb Tenses.pdf",
    "finite and non finite": "files/Finite and non finite.pdf",
    "pronouns": "files/Pronouns.pdf",
    "modifiers": "files/Modifiers.pdf",
    "run ons & fragments": "files/run ons and fragments.pdf",
    "transitions": "files/transitions.pdf",
    "transition practice": "files/Transition Practice.pdf",
    "transition practice & explanation": "files/Transition Practice & Explanation.pdf",
    "rhetorical synthesis practice": "files/Rhetorical Synthesis Practice.pdf",
    "rhetorical synthesis practice & explanation": "files/Rhetorical Synthesis Practice & Explanation.pdf",
    "test 15": "files/test 15.pdf",
    "test 15 marked": "files/test 15 marked.pdf",
    "test 16": "files/test 16.pdf",
    "test 16 marked": "files/test 16 marked.pdf",
    "test 17": "files/test 17.pdf",
    "test 17 marked": "files/test 17 marked.pdf",
    "test 18": "files/test 18.pdf",
    "test 18 marked": "files/test 18 marked.pdf",
    "vocabulary (the eloquent ones)": "files/The Eloquent Ones.pdf"
}

all_files_message = (
    "📚 *Available Files:* Copy and paste one of the names below to get the PDF:\n\n" +
    "\n".join(file_lookup.keys())
)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome!\n" + all_files_message)

# Handles user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()
    if text in file_lookup:
        try:
            with open(file_lookup[text], 'rb') as doc:
                await update.message.reply_document(document=doc)
        except FileNotFoundError:
            await update.message.reply_text("⚠️ File not found.")
    else:
        await update.message.reply_text("❌ No matching file. Check the name and try again.")

# Run the bot
if __name__ == '__main__':
    token = os.environ.get("token")  # From environment
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
