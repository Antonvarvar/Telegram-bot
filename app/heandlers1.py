from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
import app.keyboards as kb
from app.keyboards import items
storage = MemoryStorage()

cart_storage = {}
router = Router()   

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Добро пожаловать в наш магазин кросовок', reply_markup=kb.main1)
    user_id = message.from_user.id
    if user_id not in cart_storage:
        cart_storage[user_id] = {}


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', show_alert=True, reply_markup=kb.main)


@router.callback_query(F.data == 'sneakers')
async def snikers(callback:CallbackQuery):
    await callback.answer("Вы выбрали кроссовки")
    await callback.message.answer("Предложенный вариант", reply_markup=kb.main2)

@router.callback_query(F.data == 'trouses')
async def snikers(callback:CallbackQuery):
    await callback.answer("Вы выбрали штанишки")
    await callback.message.answer("Предложенный вариант", reply_markup=kb.main3)



@router.callback_query(F.data.startswith('item_'))
async def search_item(callback:CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in cart_storage:
        cart_storage[user_id] = {}

    item_name = items.get(callback.data, "Неизвестный товар")

    if item_name in cart_storage[user_id]:
        cart_storage[user_id][item_name] += 1
    else:
        cart_storage[user_id][item_name] = 1

    await callback.answer(f'{item_name} добавлен в корзину! Количество:{cart_storage[user_id][item_name]}')


@router.callback_query(F.data == 'view_cart')
async def add_item(callback: CallbackQuery):
    user_id = callback.from_user.id
    cart = cart_storage.get(user_id, {})

    if not cart:
        await callback.message.answer('Твоя корзина пуста!')
    else:
        cart_text = 'Твоя корзина:\n'
        total_items = 0
        for item_name, quantity in cart.items():
            cart_text += f"{item_name}: {quantity} шт.\n"
            total_items += quantity
        cart_text += f"\nОбщее количество товаров: {total_items}."
        await callback.message.answer(cart_text)


    await callback.answer()


