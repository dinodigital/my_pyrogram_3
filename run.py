from pyrogram import Client
from loguru import logger

from config import config
from data.models import create_db_if_not_exists

plugins = dict(root="tg_bot/handlers")
app = Client(config.APP_NAME,
             api_id=config.BOT_API_ID,
             api_hash=config.BOT_API_HASH,
             bot_token=config.BOT_TOKEN,
             plugins=plugins)

# Запуск приложения
if __name__ == "__main__":
    create_db_if_not_exists()
    logger.info("Запускаю бота")
    app.run()
