# bot.py

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TELEGRAM_BOT_TOKEN
from data_fetch import get_chfjpy_price, get_ohlc_data
from signal_engine import get_signal

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Welcome! Use /signal to get live CHF/JPY trade signals.")

def signal(update: Update, context: CallbackContext):
    df = get_ohlc_data()
    if df is None:
        update.message.reply_text("❌ Failed to retrieve data. Try again later.")
        return

    signal = get_signal(df)
    price = get_chfjpy_price()
    
    update.message.reply_text(f"""📈 *CHF/JPY*: {price:.3f}
{signal}""", parse_mode='Markdown')

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("signal", signal))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
