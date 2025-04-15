import os
import asyncio
from aiohttp import web
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Инициализация бота
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

def get_main_menu():
    buttons = [
        [KeyboardButton(text="🎨 Генерация изображений"), KeyboardButton(text="📝 Генерация текста")],
        [KeyboardButton(text="💻 Генерация кода"), KeyboardButton(text="🎥 Генерация видео")],
        [KeyboardButton(text="🎧 Генерация аудио"), KeyboardButton(text="🛠 Полезные инструменты")],
        [KeyboardButton(text="Меню")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return markup

def get_neural_network_menu():
    main = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="DALL-E"), KeyboardButton(text="ChatGPT")],
            [KeyboardButton(text="Notion AI"), KeyboardButton(text="10WEB")],
            [KeyboardButton(text="RYTR"), KeyboardButton(text="SITEGPT")],
            [KeyboardButton(text="HEY GEN"), KeyboardButton(text="GitHub Copilot")],
            [KeyboardButton(text="Sora"), KeyboardButton(text="Eleven Labs")],
            [KeyboardButton(text="Perplexity AI"), KeyboardButton(text="Назад 🔙")]
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
        "🔹 /menu — Вернуться в главное меню\n"
        "🔹 /help — Подсказки по использованию"
    )
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=get_main_menu())

@dp.message(Command("menu"))
async def send_welcome(message: types.Message):
    welcome_text = (
        "🌟 *Привет! Я бот с крутыми нейросетями!* 🌟\n\n"
        "Я помогу тебе найти полезные и прикольные нейросети для жизни! 🚀\n"
        "Выбери, что хочешь узнать:\n"
        "🔹 /list — Список всех нейросетей\n"
        "🔹 /menu — Вернуться в главное меню\n"
        "🔹 /help — Подсказки по использованию"
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
        "3. Если что-то не работает, напиши мне! 😊\n"
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
        "Пример: Я могу создать персонализированных чат-ботов: 'Напиши приветствие для сайта кофейни' — и вот результат:\n"
        "_Делает бота, который выполняет вашу задачу_ 🤖\n\n"
        "✨ *HeyGen (Генерация видео)*\n"
        "Пример: Я могу создать тебе видео: 'Создай мне человека, говорящего новости' — и вот результат:\n"
        "_Готовое видео с человеком, говорящем на любом языке_ 🎥\n\n"
        "💻 *GitHub Copilot (Генерация кода)*\n"
        "Пример: Я могу помочь с кодом: 'Напиши функцию на Python' — и вот результат:\n"
        "_Готовый рабочий код_ 💻\n\n"
        "🎥 *Sora (Генерация видео)*\n"
        "Пример: Я могу создать видео: 'Сгенерируй ролик про лес' — и вот результат:\n"
        "_Реалистичное видео с лесом_ 📹\n\n"
        "🎧 *Eleven Labs (Генерация аудио)*\n"
        "Пример: Я могу озвучить текст: 'Прочитай сказку' — и вот результат:\n"
        "_Реалистичный голос, как у человека_ 🎙️\n\n"
        "🛠 *Perplexity AI (Полезные инструменты)*\n"
        "Пример: Я могу найти информацию: 'Расскажи про космос' — и вот результат:\n"
        "_Подробный и точный ответ_ 🔍\n\n"
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
        "   - Полезность: Для вдохновения и творчества\n\n"
        "🔸 *Imagen (Google)*\n"
        "   - Описание: Создаёт фотореалистичные картинки из текста\n"
        "   - Полезность: Для реалистичных артов\n\n"
        "🔸 *Make-A-Scene (Meta)*\n"
        "   - Описание: Генерирует сцены из текста и набросков\n"
        "   - Полезность: Больше контроля над результатом\n\n"
        "🔸 *Craiyon*\n"
        "   - Описание: Простой инструмент для создания изображений из текста\n"
        "   - Полезность: Бесплатно и легко\n\n"
        "🔸 *DreamStudio*\n"
        "   - Описание: Удобный интерфейс для создания изображений с помощью ИИ\n"
        "   - Полезность: Твори без сложностей\n\n"
        "🔸 *Artbreeder*\n"
        "   - Описание: Инструмент для совместного творчества\n"
        "   - Полезность: Создавай и редактируй арты с ИИ\n\n"
        "🔸 *GauGAN2*\n"
        "   - Описание: Создаёт фотореалистичные изображения из текста и набросков\n"
        "   - Полезность: Для художников",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "midjourney_example")
async def show_midjourney_example(callback: CallbackQuery):
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
        "   - Полезность: Для поиска правдивой информации\n\n"
        "🔸 *Claude (Anthropic)*\n"
        "   - Описание: Умный чат-бот для диалогов и задач\n"
        "   - Полезность: Надёжный помощник\n\n"
        "🔸 *Vicuna-13B (#opensource)*\n"
        "   - Описание: Бесплатный чат-бот, обученный на диалогах\n"
        "   - Полезность: Для экспериментов\n\n"
        "🔸 *Mistral (#opensource)*\n"
        "   - Описание: Мощная языковая модель для текстов\n"
        "   - Полезность: Открытая и современная\n\n"
        "🔸 *Qwen (Alibaba Cloud, #opensource)*\n"
        "   - Описание: Чат-бот для текста, изображений и документов\n"
        "   - Полезность: Универсальный помощник\n\n"
        "🔸 *HyperWrite*\n"
        "   - Описание: Помощник для письма, ускоряет создание текстов\n"
        "   - Полезность: Пиши быстро\n\n"
        "🔸 *Jenni*\n"
        "   - Описание: Экономит время на текстах\n"
        "   - Полезность: Генерирует идеи и пишет за тебя\n\n"
        "🔸 *Rytr*\n"
        "   - Описание: Генерирует тексты в любом стиле с помощью ИИ\n"
        "   - Полезность: Для писем и маркетинга",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "chatgpt_example")
async def show_chatgpt_example(callback: CallbackQuery):
    await callback.message.answer("💬 ChatGPT может написать: 'Составь план на день' — и выдаст подробный список дел!")
    await callback.answer()

@dp.message(F.text == "💻 Генерация кода")
async def show_code_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Узнать больше о GitHub Copilot", url="https://github.com/features/copilot")],
        [InlineKeyboardButton(text="Пример работы", callback_data="copilot_example")]
    ])

    await message.answer(
        "💻 *Нейросети для генерации кода:*\n\n"
        "🔸 *GitHub Copilot*\n"
        "   - Описание: Помощник для программистов, предлагает код прямо в редакторе\n"
        "   - Полезность: Пиши код быстрее\n\n"
        "🔸 *OpenAI Codex*\n"
        "   - Описание: Переводит текст в код\n"
        "   - Полезность: Отлично для автоматизации\n\n"
        "🔸 *Tabnine*\n"
        "   - Описание: Ускоряет код с автодополнением\n"
        "   - Полезность: Для продуктивности\n\n"
        "🔸 *CodiumAI*\n"
        "   - Описание: Генерирует тесты для кода в IDE\n"
        "   - Полезность: Для разработчиков",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "copilot_example")
async def show_copilot_example(callback: CallbackQuery):
    await callback.message.answer("💻 GitHub Copilot может написать код, например: 'Функция на Python для сортировки списка'!")
    await callback.answer()

@dp.message(F.text == "🎥 Генерация видео")
async def show_video_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Узнать больше о Sora", url="https://openai.com/sora")],
        [InlineKeyboardButton(text="Пример работы", callback_data="sora_example")]
    ])

    await message.answer(
        "🎥 *Нейросети для генерации видео:*\n\n"
        "🔸 *Sora (OpenAI)*\n"
        "   - Описание: Создаёт реалистичные видео из текста\n"
        "   - Полезность: Оживи идеи\n\n"
        "🔸 *Runway*\n"
        "   - Описание: Инструмент для создания и редактирования видео с ИИ\n"
        "   - Полезность: Для творчества\n\n"
        "🔸 *Synthesia*\n"
        "   - Описание: Превращает текст в видео с ведущими\n"
        "   - Полезность: Быстро и профессионально\n\n"
        "🔸 *Pika*\n"
        "   - Описание: Платформа для создания видео из идей\n"
        "   - Полезность: Твори легко\n\n"
        "🔸 *HeyGen*\n"
        "   - Описание: Генерирует видео с говорящими персонажами\n"
        "   - Полезность: Для рекламы и новостей",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "sora_example")
async def show_sora_example(callback: CallbackQuery):
    await callback.message.answer("🎥 Sora может создать видео, например: 'Ролик про закат в горах'!")
    await callback.answer()

@dp.message(F.text == "🎧 Генерация аудио")
async def show_audio_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Узнать больше о Eleven Labs", url="https://elevenlabs.io")],
        [InlineKeyboardButton(text="Пример работы", callback_data="elevenlabs_example")]
    ])

    await message.answer(
        "🎧 *Нейросети для генерации аудио:*\n\n"
        "🔸 *Eleven Labs*\n"
        "   - Описание: Генерирует реалистичные голоса из текста\n"
        "   - Полезность: Для озвучки\n\n"
        "🔸 *Resemble AI*\n"
        "   - Описание: Создаёт и клонирует голоса из текста\n"
        "   - Полезность: Для подкастов\n\n"
        "🔸 *Play.ht*\n"
        "   - Описание: Превращает текст в голос\n"
        "   - Полезность: Для аудиоконтента\n\n"
        "🔸 *MusicLM (Google Research)*\n"
        "   - Описание: Генерирует музыку из текста\n"
        "   - Полезность: Для мелодий",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "elevenlabs_example")
async def show_elevenlabs_example(callback: CallbackQuery):
    await callback.message.answer("🎙️ Eleven Labs может озвучить текст, например: 'Прочитай сказку голосом робота'!")
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
        "   - Полезность: Для написания текстов без ошибок\n\n"
        "🔹 *Perplexity AI*\n"
        "   - Описание: Поисковик на ИИ, находит ответы быстро\n"
        "   - Полезность: Для исследований\n\n"
        "🔹 *Otter.ai*\n"
        "   - Описание: Записывает и расшифровывает встречи\n"
        "   - Полезность: Для продуктивности\n\n"
        "🔹 *Whisper (#opensource)*\n"
        "   - Описание: Распознаёт речь и делает текст\n"
        "   - Полезность: Для транскрипции\n\n"
        "🔹 *SiteGPT*\n"
        "   - Описание: Создаёт чат-ботов для твоего сайта\n"
        "   - Полезность: Для автоматизации поддержки",
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

@dp.message(F.text == "GitHub Copilot")
async def show_copilot_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о GitHub Copilot", url="https://github.com/features/copilot")]
    ])
    await message.answer(
        "💻 *GitHub Copilot*\n\n"
        "🔸 *Описание:* Помощник для программистов, предлагает код прямо в редакторе.\n"
        "🔸 *Пример использования:* Попроси 'Напиши функцию на Python', и Copilot напишет код.\n"
        "🔸 *Полезность:* Для быстрого написания кода и автоматизации.",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.message(F.text == "Sora")
async def show_sora_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Sora", url="https://openai.com/sora")]
    ])
    await message.answer(
        "🎥 *Sora*\n\n"
        "🔸 *Описание:* Создаёт реалистичные видео из текста.\n"
        "🔸 *Пример использования:* Попроси 'Сгенерируй ролик про лес', и Sora создаст видео.\n"
        "🔸 *Полезность:* Для создания видеоконтента и творчества.",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.message(F.text == "Eleven Labs")
async def show_elevenlabs_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Eleven Labs", url="https://elevenlabs.io")]
    ])
    await message.answer(
        "🎧 *Eleven Labs*\n\n"
        "🔸 *Описание:* Генерирует реалистичные голоса из текста.\n"
        "🔸 *Пример использования:* Попроси 'Прочитай сказку', и получишь озвучку.\n"
        "🔸 *Полезность:* Для озвучки, подкастов и аудиоконтента.",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.message(F.text == "Perplexity AI")
async def show_perplexity_details(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Perplexity AI", url="https://www.perplexity.ai")]
    ])
    await message.answer(
        "🛠 *Perplexity AI*\n\n"
        "🔸 *Описание:* Поисковик на ИИ, находит ответы быстро.\n"
        "🔸 *Пример использования:* Попроси 'Расскажи про космос', и получишь точный ответ.\n"
        "🔸 *Полезность:* Для исследований и учёбы.",
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