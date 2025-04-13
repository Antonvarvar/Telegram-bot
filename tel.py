import os
import asyncio
from aiohttp import web
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


def get_main_menu():
    buttons = [
        [KeyboardButton(text="🎨 Генерация изображений"),KeyboardButton(text="📝 Генерация текста")],
        [KeyboardButton(text="🛠 Полезные инструменты"),KeyboardButton(text="Меню")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return markup


def get_neural_network_menu():
    main = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="DALL-E"), KeyboardButton(text="ChatGPT")],
            [KeyboardButton(text="Notion AI"), KeyboardButton(text="10WEB")],
            [KeyboardButton(text="RYTR"), KeyboardButton(text="SITEGPT")],
            [KeyboardButton(text="HEY GEN")], [(KeyboardButton(text="Назад 🔙"))]
        ],
        input_field_placeholder='Выберите пункт меню...',
        resize_keyboard=True
    )
    return main


@dp.message(Command("start"))
async def send_welcome(message: Message):
    welcome_text = (
        "🌟 *Привет! Я бот с крутыми нейросетями!* 🌟\n\n"
        "Я помогу тебе найти полезные и прикольные нейросети для жизни! 🚀\n"
        "Выбери, что хочешь узнать:\n"
        "🔹 /list — Список всех нейросетей\n"
        "🔹 /help — Подсказки по использованию\n"
        "🔹 /help — Подсказки по использованию"
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=get_main_menu())

@dp.message(Command("menu"))
async def send_welcome(message:types.Message):
    welcome_text = (
        "🌟 *Привет! Я бот с крутыми нейросетями!* 🌟\n\n"
        "Я помогу тебе найти полезные и прикольные нейросети для жизни! 🚀\n"
        "Выбери, что хочешь узнать:\n"
        "🔹 /list — Список всех нейросетей\n"
        "🔹 /help — Подсказки по использованию\n"
        "🔹 /menu — Вернуться в главное меню"
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=get_main_menu())


@dp.message(F.text == "Меню")
async def menus(message: types.Message):
    welcome_text = (
        "🌟 *Привет! Я бот с крутыми нейросетями!* 🌟\n\n"
        "Я помогу тебе найти полезные и прикольные нейросети для жизни! 🚀\n"
        "Выбери, что хочешь узнать:\n"
        "🔹 /list — Список всех нейросетей\n"
        "🔹 /menu — Вернуться в главное меню\n"
        "🔹 /help — Подсказки по использованию"
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=get_main_menu())




@dp.message(Command("help"))
async def send_help(message: Message):
    help_text = (
        "ℹ️ *Как пользоваться ботом?*\n\n"
        "1. Нажми на кнопку с категорией, чтобы увидеть список нейросетей.\n"
        "2. Используй inline-кнопки, чтобы узнать больше или увидеть примеры.\n"
        "3. Если что-то не работает, напиши мне! 😊"
        "4. Используй /menu, чтобы вернуться в главное меню."
    )
    await message.answer(help_text, parse_mode="Markdown")




@dp.message(Command("list"))
async def show_list(message: Message):


    list_text = (
        "✨ *Список нейросетей с примерами работы:* ✨\n\n"
        "🖼 *DALL-E (Генерация изображений)*\n"
        "Пример: Я могу сгенерировать изображение по описанию: 'Кот в космосе' 🐱🚀\n\n"
        "📝 *ChatGPT (Генерация текста)*\n"
        "Пример: Я могу написать текст: 'Напиши письмо другу' — и вот результат:\n"
        "_Привет, как дела? Давно не виделись!_ ✍️\n\n"
        "🛠 *Notion AI (Полезные инструменты)*\n"
        "Пример: Я могу организовать твои заметки: 'Составь план на неделю' — и вот план:\n"
        "_Понедельник: Учёба, Вторник: Спорт..._ 📅\n\n"
        "✨ *10Web (Веб-сайты)*\n"
        "Пример: Я могу создать тебе сайт: 'Вот тебе критерии к сайту' — и вот результат:\n"
        "_Готовый полномодифицирующий сайт_ 🌐\n\n"
        "📝 *Rytr (Генерация текстов)*\n"
        "Пример: Я могу создать тебе текст под любой стиль: 'Напиши мне письмо для бабушки' — и вот 40 шаблонов:\n"
        "_Удобный и подходящий текст под обстоятельства_ ✍️\n\n"
        "🛠 *SiteGPT (Генерация ботов для твоего сайта)*\n"
        "Пример: Я могу создать персонализированных чат-ботов, обученных на контенте твоего сайта: 'Напиши приветствие для сайта кофейни в тёплом стиле' — и вот результат:\n"
        "_Делает бота, который выполняет вашу задачу_ 🤖\n\n"
        "✨ *HeyGen (Генерация видео)*\n"
        "Пример: Я могу создать тебе видео: 'Создай мне человека, говорящего новости' — и вот результат:\n"
        "_Готовое видео с человеком, говорящем на любом популярном языке_ 🎥\n\n"
        "Выбери нейросеть ниже, чтобы узнать больше ⬇️"
    )
    await message.answer(list_text, parse_mode="Markdown", reply_markup=get_neural_network_menu())



@dp.message(F.text == "🎨 Генерация изображений")
async def show_image_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Узнать больше о MidJourney", url="https://www.midjourney.com")],
        [InlineKeyboardButton(text="Пример работы", callback_data="midjourney_example")]
    ])

    await message.answer(
        "🖼 *Нейросети для генерации изображений:*\n\n"
        "🔸 *DALL-E*\n"
        "   - Описание: Создаёт картинки по текстовому описанию\n"
        "   - Полезность: Для креативных идей и дизайна\n\n"
        "🔸 *Stable Diffusion*\n"
        "   - Описание: Генерирует реалистичные изображения\n"
        "   - Полезность: Для создания фотореалистичных артов\n\n"
        "🔸 *MidJourney*\n"
        "   - Описание: Создаёт уникальные и креативные арты\n"
        "   - Полезность: Для вдохновения и творчества",
        parse_mode="Markdown",
        reply_markup=markup
    )



    await message.answer_photo(
        photo="https://example.com/midjourney_image.jpg",  # Замени на реальный URL
        caption="🖼 Пример работы MidJourney: 'Космический пейзаж'"
    )



@dp.callback_query(F.data == "midjourney_example")
async def show_midjourney_example(callback: types.CallbackQuery):
    await callback.message.answer("🎨 MidJourney может создать арт, например: 'Футуристический город в неоне'!")
    await callback.answer()



@dp.message(F.text == "📝 Генерация текста")
async def show_text_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Узнать больше о ChatGPT", url="https://openai.com/chatgpt")],
        [InlineKeyboardButton(text="Пример работы", callback_data="chatgpt_example")]
    ])

    await message.answer(
        "📝 *Нейросети для генерации текста:*\n\n"
        "🔸 *ChatGPT*\n"
        "   - Описание: Отвечает на вопросы, пишет тексты\n"
        "   - Полезность: Помогает с домашкой или идеями\n\n"
        "🔸 *Grok (xAI)*\n"
        "   - Описание: Даёт честные и прямые ответы\n"
        "   - Полезность: Для поиска правдивой информации",
        parse_mode="Markdown",
        reply_markup=markup
    )




@dp.callback_query(F.data == "chatgpt_example")
async def show_chatgpt_example(callback: CallbackQuery):
    await callback.message.answer("💬 ChatGPT может написать: 'Составь план на день' — и выдаст подробный список дел!")
    await callback.answer()



@dp.message(F.text == "🛠 Полезные инструменты")
async def show_tools(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Узнать больше о Notion AI", url="https://www.notion.so/product/ai")],
        [InlineKeyboardButton(text="Пример работы", callback_data="notion_example")]
    ])

    await message.answer(
        "🛠 *Полезные инструменты:*\n\n"
        "🔹 *Notion AI*\n"
        "   - Описание: Помогает организовать заметки и генерировать идеи\n"
        "   - Полезность: Для учёбы и работы\n\n"
        "🔹 *Grammarly*\n"
        "   - Описание: Проверяет грамматику и стиль текста\n"
        "   - Полезность: Для написания текстов без ошибок",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.message(F.text == "Назад 🔙")
async def go_back(message: Message):
    await message.answer(
        "✨ *Вернулся в главное меню!* ✨\n\n"
        "Выбери категорию ниже ⬇️",
        parse_mode="Markdown",
        reply_markup=get_main_menu()
    )


@dp.callback_query(F.data == "notion_example")
async def show_notion_example(callback: CallbackQuery):
    await callback.message.answer("📋 Пример: Notion AI может автоматически составить план проекта!")
    await callback.answer()



@dp.message(F.text == "DALL-E")
async def show_dalle_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о DALL-E", url="https://openai.com/dall-e")]
    ])
    await message.answer(
        "🖼 *DALL-E*\n\n"
        "🔸 *Описание:* Создаёт изображения по текстовому описанию.\n"
        "🔸 *Пример использования:* Напиши 'Кот в шляпе на Луне', и DALL-E нарисует это!\n"
        "🔸 *Полезность:* Отлично подходит для дизайнеров, художников и креативных людей.",
        parse_mode="Markdown",
        reply_markup=markup
    )



@dp.message(F.text == "ChatGPT")
async def show_chatgpt_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о ChatGPT", url="https://openai.com/chatgpt")]
    ])
    await message.answer(
        "📝 *ChatGPT*\n\n"
        "🔸 *Описание:* Генерирует текст, отвечает на вопросы, помогает с задачами.\n"
        "🔸 *Пример использования:* Может написать эссе, ответить на вопрос или составить план.\n"
        "🔸 *Полезность:* Идеально для студентов, писателей и тех, кто ищет идеи.",
        parse_mode="Markdown",
        reply_markup=markup
    )



@dp.message(F.text == "Notion AI")
async def show_notion_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Notion AI", url="https://www.notion.so/product/ai")]
    ])
    await message.answer(
        "🛠 *Notion AI*\n\n"
        "🔸 *Описание:* Помогает организовать заметки, генерировать идеи и автоматизировать задачи.\n"
        "🔸 *Пример использования:* Может составить план проекта или предложить идеи для заметок.\n"
        "🔸 *Полезность:* Для тех, кто хочет повысить продуктивность и организованность.",
        parse_mode="Markdown",
        reply_markup=markup
    )



@dp.message(F.text == "10WEB")
async def show_10web_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о 10Web", url="https://10web.io")]
    ])
    await message.answer(
        "✨ *10Web*\n\n"
        "🔸 *Описание:* Создаёт веб-сайты с помощью ИИ на основе твоих критериев.\n"
        "🔸 *Пример использования:* Дай запрос 'Сайт для кофейни в минималистичном стиле', и 10Web создаст готовый сайт.\n"
        "🔸 *Полезность:* Для быстрого создания сайтов без навыков программирования.",
        parse_mode="Markdown",
        reply_markup=markup
    )



@dp.message(F.text == "RYTR")
async def show_rytr_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Rytr", url="https://rytr.me")]
    ])
    await message.answer(
        "📝 *Rytr*\n\n"
        "🔸 *Описание:* Генерирует тексты в любом стиле с помощью ИИ.\n"
        "🔸 *Пример использования:* Попроси 'Напиши письмо для бабушки', и Rytr предложит 40 шаблонов.\n"
        "🔸 *Полезность:* Для создания текстов, от писем до маркетинговых материалов.",
        parse_mode="Markdown",
        reply_markup=markup
    )



@dp.message(F.text == "SITEGPT")
async def show_sitegpt_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о SiteGPT", url="https://sitegpt.ai")]
    ])
    await message.answer(
        "🛠 *SiteGPT*\n\n"
        "🔸 *Описание:* Создаёт персонализированных чат-ботов, обученных на контенте твоего сайта.\n"
        "🔸 *Пример использования:* Попроси 'Приветствие для сайта кофейни в тёплом стиле', и SiteGPT создаст бота.\n"
        "🔸 *Полезность:* Для автоматизации поддержки и улучшения взаимодействия с клиентами.",
        parse_mode="Markdown",
        reply_markup=markup
    )



@dp.message(F.text == "HEY GEN")
async def show_heygen_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о HeyGen", url="https://www.heygen.com")]
    ])
    await message.answer(
        "✨ *HeyGen*\n\n"
        "🔸 *Описание:* Генерирует видео с помощью ИИ, включая говорящих персонажей.\n"
        "🔸 *Пример использования:* Попроси 'Создай человека, говорящего новости', и HeyGen создаст видео.\n"
        "🔸 *Полезность:* Для создания видеоконтента, от рекламы до новостей, на разных языках.",
        parse_mode="Markdown",
        reply_markup=markup
    )



async def health_check(request):
    return web.Response(text="Bot is running")

app = web.Application()
app.router.add_get("/", health_check)

async def start_webserver():
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    await start_webserver()
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("Бот остановлен пользователем.")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())