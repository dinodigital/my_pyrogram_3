from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def easy_inline_markup(buttons=None):
    """
    Упрощенная генерация inline клавиатуры.

    1 кнопка
    [[(text, callback)]]

    2 кнопки в сроке
    [[(text, callback), (text, callback)]]

    2 строки по 2 кнопки
    [
        [("Да", "callback_yes"), ("Нет", "callback_no")],
        [("1", "callback_1"), ("2", "callback_2")],
    ]

    Кнопка с url
    ("Название кнопки", "http://ссылка", "url")
    """

    # Кнопка закрыть
    if not buttons:
        return InlineKeyboardMarkup([[InlineKeyboardButton(text="» Скрыть «", callback_data="close")]])

    bot_buttons = []
    for row in buttons:
        bot_row = []
        for button in row:
            if 'url' in button:
                bot_row.append(InlineKeyboardButton(text=button[0], url=button[1]))
            else:
                bot_row.append(InlineKeyboardButton(text=button[0], callback_data=button[1]))
        bot_buttons.append(bot_row)

    return InlineKeyboardMarkup(bot_buttons)


def url_button(button):
    """
    Кнопка со ссылкой
    """
    return InlineKeyboardMarkup([[InlineKeyboardButton(text=button[0], url=button[1])]])


def with_close_btn():
    """
    Кнопка удаления сообщения
    """
    return InlineKeyboardMarkup([[InlineKeyboardButton(text="» Скрыть «", callback_data="close")]])


