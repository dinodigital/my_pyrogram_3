from pyrogram import filters
from config import config


def admin_filter(_, __, message):
    return message.from_user.id in config.ADMINS


admin_filter = filters.create(admin_filter)
