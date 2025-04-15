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
        "2. Используй inline-кнопки, чтобы узнать больше о нейросетях.\n"
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

# Обработчики категорий с inline-кнопками
@dp.message(F.text == "🎨 Генерация изображений")
async def show_image_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="DALL-E", callback_data="image_dalle")],
        [InlineKeyboardButton(text="Stable Diffusion", callback_data="image_stablediffusion")],
        [InlineKeyboardButton(text="MidJourney", callback_data="image_midjourney")],
        [InlineKeyboardButton(text="Imagen (Google)", callback_data="image_imagen")],
        [InlineKeyboardButton(text="Make-A-Scene (Meta)", callback_data="image_makeascene")],
        [InlineKeyboardButton(text="Craiyon", callback_data="image_craiyon")],
        [InlineKeyboardButton(text="DreamStudio", callback_data="image_dreamstudio")],
        [InlineKeyboardButton(text="Artbreeder", callback_data="image_artbreeder")],
        [InlineKeyboardButton(text="GauGAN2", callback_data="image_gaugan2")]
    ])

    await message.answer(
        "🖼 *Нейросети для генерации изображений:*\n\n"
        "Выбери нейросеть, чтобы узнать подробности ⬇️",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "image_dalle")
async def show_image_dalle_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о DALL-E", url="https://openai.com/dall-e")]
    ])
    await callback.message.answer(
        "🖼 *DALL-E*\n\n"
        "🔸 *Описание:* Создаёт картинки по текстовому описанию.\n"
        "🔸 *Пример использования:* Напиши 'Кот в шляпе на Луне', и DALL-E нарисует это!\n"
        "🔸 *Полезность:* Для креативных идей и дизайна.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "image_stablediffusion")
async def show_image_stablediffusion_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Stable Diffusion", url="https://stability.ai/stable-diffusion")]
    ])
    await callback.message.answer(
        "🖼 *Stable Diffusion*\n\n"
        "🔸 *Описание:* Генерирует реалистичные изображения.\n"
        "🔸 *Пример использования:* Создай фотореалистичный портрет или пейзаж.\n"
        "🔸 *Полезность:* Для создания фотореалистичных артов.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "image_midjourney")
async def show_image_midjourney_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о MidJourney", url="https://www.midjourney.com")]
    ])
    await callback.message.answer(
        "🖼 *MidJourney*\n\n"
        "🔸 *Описание:* Создаёт уникальные и креативные арты.\n"
        "🔸 *Пример использования:* Сгенерируй арт 'Футуристический город в неоне'.\n"
        "🔸 *Полезность:* Для вдохновения и творчества.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "image_imagen")
async def show_image_imagen_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Imagen", url="https://cloud.google.com/blog/topics/developers-practitioners/introducing-imagen-2")]
    ])
    await callback.message.answer(
        "🖼 *Imagen *\n\n"
        "🔸 *Описание:* Создаёт фотореалистичные картинки из текста.\n"
        "🔸 *Пример использования:* Сгенерируй реалистичный пейзаж по описанию.\n"
        "🔸 *Полезность:* Для реалистичных артов.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "image_makeascene")
async def show_image_makeascene_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Make-A-Scene", url="https://ai.meta.com/blog/make-a-scene-ai-powered-image-generation/")]
    ])
    await callback.message.answer(
        "🖼 *Make-A-Scene*\n\n"
        "🔸 *Описание:* Генерирует сцены из текста и набросков.\n"
        "🔸 *Пример использования:* Создай сцену 'Закат над горами' с наброском.\n"
        "🔸 *Полезность:* Больше контроля над результатом.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "image_craiyon")
async def show_image_craiyon_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Craiyon", url="https://www.craiyon.com")]
    ])
    await callback.message.answer(
        "🖼 *Craiyon*\n\n"
        "🔸 *Описание:* Простой инструмент для создания изображений из текста.\n"
        "🔸 *Пример использования:* Сгенерируй картинку 'Собака в парке'.\n"
        "🔸 *Полезность:* Бесплатно и легко.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "image_dreamstudio")
async def show_image_dreamstudio_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о DreamStudio", url="https://dreamstudio.ai")]
    ])
    await callback.message.answer(
        "🖼 *DreamStudio*\n\n"
        "🔸 *Описание:* Удобный интерфейс для создания изображений с помощью ИИ.\n"
        "🔸 *Пример использования:* Создай арт 'Фантастический лес'.\n"
        "🔸 *Полезность:* Твори без сложностей.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "image_artbreeder")
async def show_image_artbreeder_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Artbreeder", url="https://www.artbreeder.com")]
    ])
    await callback.message.answer(
        "🖼 *Artbreeder*\n\n"
        "🔸 *Описание:* Инструмент для совместного творчества.\n"
        "🔸 *Пример использования:* Создай и отредактируй портрет или пейзаж.\n"
        "🔸 *Полезность:* Создавай и редактируй арты с ИИ.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "image_gaugan2")
async def show_image_gaugan2_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о GauGAN2", url="http://gaugan.org/gaugan2/")]
    ])
    await callback.message.answer(
        "🖼 *GauGAN2*\n\n"
        "🔸 *Описание:* Создаёт фотореалистичные изображения из текста и набросков.\n"
        "🔸 *Пример использования:* Сгенерируй пейзаж 'Озеро в горах'.\n"
        "🔸 *Полезность:* Для художников.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.message(F.text == "📝 Генерация текста")
async def show_text_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="ChatGPT", callback_data="text_chatgpt")],
        [InlineKeyboardButton(text="Grok (xAI)", callback_data="text_grok")],
        [InlineKeyboardButton(text="Claude (Anthropic)", callback_data="text_claude")],
        [InlineKeyboardButton(text="Vicuna-13B", callback_data="text_vicuna")],
        [InlineKeyboardButton(text="Mistral", callback_data="text_mistral")],
        [InlineKeyboardButton(text="Qwen (Alibaba Cloud)", callback_data="text_qwen")],
        [InlineKeyboardButton(text="HyperWrite", callback_data="text_hyperwrite")],
        [InlineKeyboardButton(text="Jenni", callback_data="text_jenni")],
        [InlineKeyboardButton(text="Rytr", callback_data="text_rytr")]
    ])

    await message.answer(
        "📝 *Нейросети для генерации текста:*\n\n"
        "Выбери нейросеть, чтобы узнать подробности ⬇️",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "text_chatgpt")
async def show_text_chatgpt_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о ChatGPT", url="https://openai.com/chatgpt")]
    ])
    await callback.message.answer(
        "📝 *ChatGPT*\n\n"
        "🔸 *Описание:* Отвечает на вопросы, пишет тексты.\n"
        "🔸 *Пример использования:* Может написать эссе или составить план.\n"
        "🔸 *Полезность:* Помогает с домашкой или идеями.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "text_grok")
async def show_text_grok_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Grok", url="https://x.ai/grok")]
    ])
    await callback.message.answer(
        "📝 *Grok)*\n\n"
        "🔸 *Описание:* Даёт честные и прямые ответы.\n"
        "🔸 *Пример использования:* Попроси 'Расскажи правду о космосе'.\n"
        "🔸 *Полезность:* Для поиска правдивой информации.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "text_claude")
async def show_text_claude_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Claude", url="https://www.anthropic.com/claude")]
    ])
    await callback.message.answer(
        "📝 *Claude *\n\n"
        "🔸 *Описание:* Умный чат-бот для диалогов и задач.\n"
        "🔸 *Пример использования:* Попроси 'Помоги с планом проекта'.\n"
        "🔸 *Полезность:* Надёжный помощник.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "text_vicuna")
async def show_text_vicuna_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Vicuna-13B", url="https://github.com/lm-sys/vicuna-13b")]
    ])
    await callback.message.answer(
        "📝 *Vicuna-13B*\n\n"
        "🔸 *Описание:* Бесплатный чат-бот, обученный на диалогах.\n"
        "🔸 *Пример использования:* Попроси 'Проведи диалог на тему космоса'.\n"
        "🔸 *Полезность:* Для экспериментов.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "text_mistral")
async def show_text_mistral_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Mistral", url="https://mistral.ai")]
    ])
    await callback.message.answer(
        "📝 *Mistral*\n\n"
        "🔸 *Описание:* Мощная языковая модель для текстов.\n"
        "🔸 *Пример использования:* Попроси 'Напиши статью про ИИ'.\n"
        "🔸 *Полезность:* Открытая и современная.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "text_qwen")
async def show_text_qwen_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Qwen", url="https://www.alibabacloud.com/en/product/qwen")]
    ])
    await callback.message.answer(
        "📝 *Qwen*\n\n"
        "🔸 *Описание:* Чат-бот для текста, изображений и документов.\n"
        "🔸 *Пример использования:* Попроси 'Составь отчёт из документа'.\n"
        "🔸 *Полезность:* Универсальный помощник.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "text_hyperwrite")
async def show_text_hyperwrite_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о HyperWrite", url="https://hyperwrite.ai")]
    ])
    await callback.message.answer(
        "📝 *HyperWrite*\n\n"
        "🔸 *Описание:* Помощник для письма, ускоряет создание текстов.\n"
        "🔸 *Пример использования:* Попроси 'Напиши черновик письма'.\n"
        "🔸 *Полезность:* Пиши быстро.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "text_jenni")
async def show_text_jenni_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Jenni", url="https://jenni.ai")]
    ])
    await callback.message.answer(
        "📝 *Jenni*\n\n"
        "🔸 *Описание:* Экономит время на текстах.\n"
        "🔸 *Пример использования:* Попроси 'Сгенерируй идеи для статьи'.\n"
        "🔸 *Полезность:* Генерирует идеи и пишет за тебя.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "text_rytr")
async def show_text_rytr_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Rytr", url="https://rytr.me")]
    ])
    await callback.message.answer(
        "📝 *Rytr*\n\n"
        "🔸 *Описание:* Генерирует тексты в любом стиле с помощью ИИ.\n"
        "🔸 *Пример использования:* Попроси 'Напиши письмо для бабушки'.\n"
        "🔸 *Полезность:* Для писем и маркетинга.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.message(F.text == "💻 Генерация кода")
async def show_code_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="GitHub Copilot", callback_data="code_copilot")],
        [InlineKeyboardButton(text="OpenAI Codex", callback_data="code_codex")],
        [InlineKeyboardButton(text="Tabnine", callback_data="code_tabnine")],
        [InlineKeyboardButton(text="CodiumAI", callback_data="code_codiumai")]
    ])

    await message.answer(
        "💻 *Нейросети для генерации кода:*\n\n"
        "Выбери нейросеть, чтобы узнать подробности ⬇️",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "code_copilot")
async def show_code_copilot_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о GitHub Copilot", url="https://github.com/features/copilot")]
    ])
    await callback.message.answer(
        "💻 *GitHub Copilot*\n\n"
        "🔸 *Описание:* Помощник для программистов, предлагает код прямо в редакторе.\n"
        "🔸 *Пример использования:* Попроси 'Напиши функцию на Python'.\n"
        "🔸 *Полезность:* Пиши код быстрее.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "code_codex")
async def show_code_codex_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о OpenAI Codex", url="https://openai.com/blog/openai-codex")]
    ])
    await callback.message.answer(
        "💻 *OpenAI Codex*\n\n"
        "🔸 *Описание:* Переводит текст в код.\n"
        "🔸 *Пример использования:* Попроси 'Напиши код для игры'.\n"
        "🔸 *Полезность:* Отлично для автоматизации.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "code_tabnine")
async def show_code_tabnine_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Tabnine", url="https://www.tabnine.com")]
    ])
    await callback.message.answer(
        "💻 *Tabnine*\n\n"
        "🔸 *Описание:* Ускоряет код с автодополнением.\n"
        "🔸 *Пример использования:* Автодополнение кода в IDE.\n"
        "🔸 *Полезность:* Для продуктивности.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "code_codiumai")
async def show_code_codiumai_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о CodiumAI", url="https://www.codium.ai")]
    ])
    await callback.message.answer(
        "💻 *CodiumAI*\n\n"
        "🔸 *Описание:* Генерирует тесты для кода в IDE.\n"
        "🔸 *Пример использования:* Попроси 'Сгенерируй тесты для функции'.\n"
        "🔸 *Полезность:* Для разработчиков.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.message(F.text == "🎥 Генерация видео")
async def show_video_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Sora (OpenAI)", callback_data="video_sora")],
        [InlineKeyboardButton(text="Runway", callback_data="video_runway")],
        [InlineKeyboardButton(text="Synthesia", callback_data="video_synthesia")],
        [InlineKeyboardButton(text="Pika", callback_data="video_pika")],
        [InlineKeyboardButton(text="HeyGen", callback_data="video_heygen")]
    ])

    await message.answer(
        "🎥 *Нейросети для генерации видео:*\n\n"
        "Выбери нейросеть, чтобы узнать подробности ⬇️",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "video_sora")
async def show_video_sora_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Sora", url="https://openai.com/sora")]
    ])
    await callback.message.answer(
        "🎥 *Sora*\n\n"
        "🔸 *Описание:* Создаёт реалистичные видео из текста.\n"
        "🔸 *Пример использования:* Попроси 'Сгенерируй ролик про лес'.\n"
        "🔸 *Полезность:* Оживи идеи.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "video_runway")
async def show_video_runway_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Runway", url="https://runwayml.com")]
    ])
    await callback.message.answer(
        "🎥 *Runway*\n\n"
        "🔸 *Описание:* Инструмент для создания и редактирования видео с ИИ.\n"
        "🔸 *Пример использования:* Отредактируй видео или создай ролик.\n"
        "🔸 *Полезность:* Для творчества.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "video_synthesia")
async def show_video_synthesia_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Synthesia", url="https://www.synthesia.io")]
    ])
    await callback.message.answer(
        "🎥 *Synthesia*\n\n"
        "🔸 *Описание:* Превращает текст в видео с ведущими.\n"
        "🔸 *Пример использования:* Создай ролик 'Ведущий читает новости'.\n"
        "🔸 *Полезность:* Быстро и профессионально.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "video_pika")
async def show_video_pika_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Pika", url="https://pika.art")]
    ])
    await callback.message.answer(
        "🎥 *Pika*\n\n"
        "🔸 *Описание:* Платформа для создания видео из идей.\n"
        "🔸 *Пример использования:* Создай видео 'Котик играет с мячом'.\n"
        "🔸 *Полезность:* Твори легко.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "video_heygen")
async def show_video_heygen_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о HeyGen", url="https://www.heygen.com")]
    ])
    await callback.message.answer(
        "🎥 *HeyGen*\n\n"
        "🔸 *Описание:* Генерирует видео с говорящими персонажами.\n"
        "🔸 *Пример использования:* Попроси 'Создай человека, говорящего новости'.\n"
        "🔸 *Полезность:* Для рекламы и новостей.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.message(F.text == "🎧 Генерация аудио")
async def show_audio_gen(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Eleven Labs", callback_data="audio_elevenlabs")],
        [InlineKeyboardButton(text="Resemble AI", callback_data="audio_resemble")],
        [InlineKeyboardButton(text="Play.ht", callback_data="audio_playht")],
        [InlineKeyboardButton(text="MusicLM (Google Research)", callback_data="audio_musiclm")]
    ])

    await message.answer(
        "🎧 *Нейросети для генерации аудио:*\n\n"
        "Выбери нейросеть, чтобы узнать подробности ⬇️",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "audio_elevenlabs")
async def show_audio_elevenlabs_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Eleven Labs", url="https://elevenlabs.io")]
    ])
    await callback.message.answer(
        "🎧 *Eleven Labs*\n\n"
        "🔸 *Описание:* Генерирует реалистичные голоса из текста.\n"
        "🔸 *Пример использования:* Попроси 'Прочитай сказку'.\n"
        "🔸 *Полезность:* Для озвучки.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "audio_resemble")
async def show_audio_resemble_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Resemble AI", url="https://www.resemble.ai")]
    ])
    await callback.message.answer(
        "🎧 *Resemble AI*\n\n"
        "🔸 *Описание:* Создаёт и клонирует голоса из текста.\n"
        "🔸 *Пример использования:* Попроси 'Озвучь подкаст'.\n"
        "🔸 *Полезность:* Для подкастов.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "audio_playht")
async def show_audio_playht_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Play.ht", url="https://play.ht")]
    ])
    await callback.message.answer(
        "🎧 *Play.ht*\n\n"
        "🔸 *Описание:* Превращает текст в голос.\n"
        "🔸 *Пример использования:* Попроси 'Озвучь статью'.\n"
        "🔸 *Полезность:* Для аудиоконтента.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "audio_musiclm")
async def show_audio_musiclm_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о MusicLM", url="https://google-research.github.io/seanet/musiclm/examples/")]
    ])
    await callback.message.answer(
        "🎧 *MusicLM*\n\n"
        "🔸 *Описание:* Генерирует музыку из текста.\n"
        "🔸 *Пример использования:* Попроси 'Сгенерируй мелодию в стиле джаз'.\n"
        "🔸 *Полезность:* Для мелодий.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.message(F.text == "🛠 Полезные инструменты")
async def show_tools(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Notion AI", callback_data="tools_notion")],
        [InlineKeyboardButton(text="Grammarly", callback_data="tools_grammarly")],
        [InlineKeyboardButton(text="Perplexity AI", callback_data="tools_perplexity")],
        [InlineKeyboardButton(text="Otter.ai", callback_data="tools_otter")],
        [InlineKeyboardButton(text="Whisper", callback_data="tools_whisper")],
        [InlineKeyboardButton(text="SiteGPT", callback_data="tools_sitegpt")]
    ])

    await message.answer(
        "🛠 *Полезные инструменты:*\n\n"
        "Выбери нейросеть, чтобы узнать подробности ⬇️",
        parse_mode="Markdown",
        reply_markup=markup
    )

@dp.callback_query(F.data == "tools_notion")
async def show_tools_notion_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Notion AI", url="https://www.notion.so/product/ai")]
    ])
    await callback.message.answer(
        "🛠 *Notion AI*\n\n"
        "🔸 *Описание:* Помогает организовать заметки, генерировать идеи.\n"
        "🔸 *Пример использования:* Попроси 'Составь план проекта'.\n"
        "🔸 *Полезность:* Для учёбы и работы.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "tools_grammarly")
async def show_tools_grammarly_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Grammarly", url="https://www.grammarly.com")]
    ])
    await callback.message.answer(
        "🛠 *Grammarly*\n\n"
        "🔸 *Описание:* Проверяет грамматику и стиль текста.\n"
        "🔸 *Пример использования:* Исправь ошибки в тексте.\n"
        "🔸 *Полезность:* Для текстов без ошибок.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "tools_perplexity")
async def show_tools_perplexity_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Perplexity AI", url="https://www.perplexity.ai")]
    ])
    await callback.message.answer(
        "🛠 *Perplexity AI*\n\n"
        "🔸 *Описание:* Поисковик на ИИ, находит ответы быстро.\n"
        "🔸 *Пример использования:* Попроси 'Расскажи про космос'.\n"
        "🔸 *Полезность:* Для исследований.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "tools_otter")
async def show_tools_otter_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Otter.ai", url="https://otter.ai")]
    ])
    await callback.message.answer(
        "🛠 *Otter.ai*\n\n"
        "🔸 *Описание:* Записывает и расшифровывает встречи.\n"
        "🔸 *Пример использования:* Расшифруй аудиозапись встречи.\n"
        "🔸 *Полезность:* Для продуктивности.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "tools_whisper")
async def show_tools_whisper_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о Whisper", url="https://openai.com/research/whisper")]
    ])
    await callback.message.answer(
        "🛠 *Whisper*\n\n"
        "🔸 *Описание:* Распознаёт речь и делает текст.\n"
        "🔸 *Пример использования:* Преобразуй аудио в текст.\n"
        "🔸 *Полезность:* Для транскрипции.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.callback_query(F.data == "tools_sitegpt")
async def show_tools_sitegpt_details(callback: CallbackQuery):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подробнее о SiteGPT", url="https://sitegpt.ai")]
    ])
    await callback.message.answer(
        "🛠 *SiteGPT*\n\n"
        "🔸 *Описание:* Создаёт чат-ботов для твоего сайта.\n"
        "🔸 *Пример использования:* Попроси 'Приветствие для сайта кофейни'.\n"
        "🔸 *Полезность:* Для автоматизации поддержки.",
        parse_mode="Markdown",
        reply_markup=markup
    )
    await callback.answer()

@dp.message(F.text == "Назад 🔙")
async def go_back(message: Message):
    await message.answer(
        "✨ *Вернулся в главное меню!* ✨\n\n"
        "Выбери категорию ниже ⬇️",
        parse_mode="Markdown",
        reply_markup=get_main_menu()
    )

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