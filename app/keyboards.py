from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(buttons=[
        [KeyboardButton(text="DALL-E")],
        [KeyboardButton(text="ChatGPT")],
        [KeyboardButton(text="DALL-E")],
        [KeyboardButton(text="10WEB")],
        [KeyboardButton(text="RYTR")],
        [KeyboardButton(text="SITEGPT")],
        [KeyboardButton(text="HEY GEN")]
    ]input_field_placeholder='Выберите пункт меню...', resize_keyboard=True)