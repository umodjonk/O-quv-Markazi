from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



rating = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "👍 Ajoyib", callback_data="great"),
            InlineKeyboardButton(text = "👎 Yomon", callback_data="bad")
        ]
    ]
)


check = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text ="Ha 👍", callback_data="yes"),
            InlineKeyboardButton(text ="Ha 👍",callback_data="no")
        ]
    ]
)