import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

from data.models import User
from tg_bot.handlers import txt
from tg_bot.helpers.markup import easy_inline_markup



@Client.on_message(~filters.bot & filters.command("start"))
def start(cli: Client, message: Message):

    tg_id = message.from_user.id

    user = User.get_or_none()
    if user is None:
        User.create(**{
            'tg_id': tg_id
        })

    message.reply(txt.hello("Человек"), reply_markup=easy_inline_markup())

    raise pyrogram.StopPropagation


@Client.on_callback_query()
def notif_no_comments_handler(cli: Client, q: CallbackQuery):
    if q.data == "close":
        q.message.delete()


@Client.on_message(~filters.bot)
def lesson_canceled_message_handler(cli: Client, message: Message):
    tg_id = message.from_user.id
    text = message.text
