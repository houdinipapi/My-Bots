from telegram.ext import Updater, CommandHandler, CallbackContext, Application
from telegram import Update
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the .env file
TOKEN = os.getenv("TELEGRAM_API_KEY")


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I'm Houdini the Bot!")

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Use /start to test me!")


def main():
    # Create an Application object
    application = Application.builder().token(TOKEN).build()

    # Add a command handler for the /start command
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Start the bot
    application.run_polling()


if __name__ == "__main__":
    main()
