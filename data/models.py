import pathlib
from datetime import datetime
from loguru import logger

import peewee

from config.config import DB_PATH

main_db = peewee.SqliteDatabase(DB_PATH)


class BaseModel(peewee.Model):
    class Meta:
        database = main_db


class User(BaseModel):
    created = peewee.DateTimeField(default=datetime.now)
    tg_id = peewee.IntegerField(default=None, null=True)


def create_db_if_not_exists():
    """
    Создает новую базу данных SQLite, если такой нет
    """
    logger.info(f"Проверяю наличие базы данных: {DB_PATH}")

    # Проверка на наличие файла БД
    if pathlib.Path(DB_PATH).exists():
        logger.info(f"База данных найдена")
        return False

    # Создание БД
    logger.info(f"База данных не найдена. Создаю новую.")
    my_db = peewee.SqliteDatabase(DB_PATH)
    my_db.connect()
    my_db.create_tables([User, ])  # Тут таблицы, которые создаем
    my_db.close()
    return True
