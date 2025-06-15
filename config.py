# config.py

from dotenv import load_dotenv
import os

load_dotenv()  # load from .env

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TWELVE_DATA_API_KEY = os.getenv("TWELVE_DATA_API_KEY")
