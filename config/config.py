import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = os.path.join(ROOT_DIR, "data/main.db")

# Telegram
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_BOT_TOKEN = os.environ.get('CHAT_BOT_TOKEN')
BOT_API_ID = os.environ.get('BOT_API_ID')
BOT_API_HASH = os.environ.get('BOT_API_HASH')

# Общие настройки
APP_NAME = "My bot"
ADMINS = [000000]

