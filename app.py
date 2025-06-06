import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler
)
from obd_database import OBDDatabase

# Initialize database
obd_db = OBDDatabase()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with command options"""
    welcome_msg = (
        "🔧 <b>OBD-II & Car Complaint Bot</b>\n\n"
        "Send:\n"
        "- An OBD code (e.g. <code>P0300</code>)\n"
        "- Or describe your car problem\n"
        "- Or use commands below:\n\n"
        "<b>Commands:</b>\n"
        "/start - Show this message\n"
        "/complaints - List common issues\n"
        "/search - Find OBD codes"
    )
    await update.message.reply_html(welcome_msg)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hybrid OBD code and AI complaint handler"""
    text = update.message.text.strip()
    
    # First check for OBD codes
    if code_info := obd_db.lookup_code(text):
        response = _format_code_response(code_info)
    else:
        # AI complaint matching
        complaint, confidence = obd_db.find_closest_complaint(text)
        response = _format_complaint_response(complaint, confidence)
    
    await update.message.reply_html(response)

def _format_code_response(info: Dict) -> str:
    """Format OBD code information"""
    return (
        f"🚗 <b>{info['description']}</b>\n"
        f"⚡ <i>Severity:</i> {info['severity']}\n\n"
        f"🔧 <i>Causes:</i>\n- " + "\n- ".join(info['causes']) + "\n\n"
        f"🛠️ <i>Solutions:</i>\n- " + "\n- ".join(info['fixes'])
    )

def _format_complaint_response(complaint: Dict, confidence: float) -> str:
    """Format AI-matched complaint"""
    if confidence < 0.4:
        return "⚠️ <i>Couldn't identify the issue clearly. Try rephrasing or use /complaints</i>"
    
    return (
        f"🔍 <b>Identified Issue:</b> {complaint['egyptian']}\n"
        f"🇬🇧 <i>{complaint['english']}</i>\n\n"
        f"💡 <b>Suggested Solutions:</b>\n"
        f"- Check related components\n"
        f"- Consult mechanic for diagnosis\n"
        f"<i>(Confidence: {confidence:.0%})</i>"
    )

def main():
    """Start the bot"""
    app = ApplicationBuilder() \
        .token(os.getenv("TELEGRAM_BOT_TOKEN")) \
        .build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is running with hybrid AI matching...")
    app.run_polling()

if __name__ == "__main__":
    main()
