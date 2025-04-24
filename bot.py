from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

# File names mapped to file paths
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

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "👋 Welcome!\n"
        "Type the file name exactly to receive its PDF.\n\n"
        "📄 *This is all the available things (copy and paste into the chat box):*\n"
        "words in context\n"
        "text structure and purpose\n"
        "cross text connection answers\n"
        "form, structure, sense annotation\n"
        "central ideas and details\n"
        "command of evidence textual\n"
        "command of evidence quantitative\n"
        "command of evidence quantitative practice\n"
        "inference\n"
        "inference answers\n"
        "punctuation\n"
        "punctuation (no answer)\n"
        "subject-verb agreement\n"
        "verb tenses\n"
        "finite and non finite\n"
        "pronouns\n"
        "modifiers\n"
        "run ons & fragments\n"
        "transitions\n"
        "transition practice\n"
        "transition practice & explanation\n"
        "rhetorical synthesis practice\n"
        "rhetorical synthesis practice & explanation\n"
        "test 15\n"
        "test 15 marked\n"
        "test 16\n"
        "test 16 marked\n"
        "test 17\n"
        "test 17 marked\n"
        "test 18\n"
        "test 18 marked\n"
        "vocabulary (the eloquent ones)"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

# Handle messages with file names
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()

    if text in file_lookup:
        file_path = file_lookup[text]
        try:
            with open(file_path, 'rb') as doc:
                await update.message.reply_document(document=doc)
        except FileNotFoundError:
            await update.message.reply_text("⚠️ File not found on server.")
        except Exception as e:
            await update.message.reply_text(f"⚠️ Error: {str(e)}")
    else:
        await update.message.reply_text("❌ File not found. Please check the name and try again.")

# Run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token("8038937835:AAH6Mg7B9GvAHtYHS0Vyez5n3r5qgIwY5Kw").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()
