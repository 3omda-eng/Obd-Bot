import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
from obd_database import OBDDatabase  # Your existing database class

# Initialize OBD code database
obd_db = OBDDatabase()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with instructions"""
    await update.message.reply_text(
        "🔧 *OBD-II Diagnostic Bot*\n\n"
        "Send me any OBD-II trouble code (e.g., P0300, C0040) and I'll provide:\n"
        "- Detailed description\n"
        "- Possible causes\n"
        "- Recommended fixes\n\n"
        "Try these commands:\n"
        "/start - Show this message\n"
        "/search [keyword] - Find codes by description\n"
        "/random - Get a random code to learn",
        parse_mode='Markdown'
    )

async def handle_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Process OBD code lookup requests"""
    user_code = update.message.text.strip().upper()
    
    # Special case for codes without prefix (e.g., "0300")
    if len(user_code) == 4 and user_code.isdigit():
        user_code = 'P' + user_code
    
    if code_info := obd_db.lookup_code(user_code):
        response = (
            f"🚗 *{user_code} - {code_info['description']}*\n"
            f"⚡ Severity: {code_info['severity']}\n\n"
            "🔧 *Possible Causes:*\n- " + "\n- ".join(code_info['causes']) + "\n\n"
            "🛠️ *Recommended Fixes:*\n- " + "\n- ".join(code_info['fixes'])
        )
    else:
        response = f"❌ Code '{user_code}' not found. Try /search [keyword]"
    
    await update.message.reply_text(response, parse_mode='Markdown')

async def search_codes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /search command"""
    if not context.args:
        await update.message.reply_text("Please enter a search term after /search")
        return
    
    keyword = " ".join(context.args)
    matches = obd_db.search_codes(keyword)
    
    if matches:
        response = "🔍 *Search Results:*\n\n" + "\n".join(
            f"- {m['code']}: {m['description']}" for m in matches
        )
    else:
        response = f"No codes found matching '{keyword}'"
    
    await update.message.reply_text(response, parse_mode='Markdown')

async def random_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random OBD code for learning"""
    import random
    all_codes = obd_db.get_all_codes()
    random_code = random.choice(all_codes)
    code_info = obd_db.lookup_code(random_code)
    
    response = (
        "🎲 *Random OBD Code*\n\n"
        f"🚗 *{random_code} - {code_info['description']}*\n"
        f"⚡ Severity: {code_info['severity']}\n\n"
        "🔧 *Possible Causes:*\n- " + "\n- ".join(code_info['causes'][:3]) + "\n\n"
        "💡 Try sending this code alone for full details"
    )
    await update.message.reply_text(response, parse_mode='Markdown')

def main():
    """Start the bot"""
    # Get token from environment variable
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("No TELEGRAM_BOT_TOKEN environment variable set")
    
    # Build application
    app = ApplicationBuilder().token(token).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("search", search_codes))
    app.add_handler(CommandHandler("random", random_code))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_code))
    
    # Start polling (for Render background worker)
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
