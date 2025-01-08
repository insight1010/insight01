import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.enums import ParseMode

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загружаем переменные окружения
load_dotenv()

# Инициализация бота
TOKEN = '8080333568:AAEkNMsbO54J7rUphZYgxWiMkpFp9rC1fp8'
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ID канала
CHANNEL_ID = -1002331485643

# Единый обработчик команды /start
@dp.message(Command('start'))
async def start(message: types.Message):
    try:
        logger.info(f"Получена команда /start от пользователя {message.from_user.id}")
        # Создаем кнопку для TMA
        webapp_button = InlineKeyboardButton(
            text='Открыть приложение 🚀',
            web_app=WebAppInfo(url='https://insight1010.github.io/insight01/')
        )
        
        # Создаем клавиатуру с кнопкой
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[webapp_button]])
        
        # Отправляем приветственное фото с текстом и кнопкой
        await message.answer_photo(
            photo='https://i.pinimg.com/736x/0d/f2/ec/0df2ec2920cb9276657967121ade978e.jpg',
            caption="🌟 *Добро пожаловать в мир инноваций!*\n\n"
                   "Я — чат бот ПРИЗ\n"
                   "(Практические Решения Изобретательских Задач).\n\n"
                   "ПРИЗ — это инновационный инструмент, который поможет вам:\n"
                   "• Находить креативные решения\n"
                   "• Развивать новые идеи\n"
                   "• Создавать уникальные проекты\n\n"
                   "Нажмите на кнопку ниже, чтобы начать работу с приложением 👇",
            parse_mode="Markdown",
            reply_markup=keyboard
        )
        logger.info(f"Успешно отправлено приветственное сообщение пользователю {message.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка в команде /start: {str(e)}")
        await message.answer("Произошла ошибка при обработке команды. Пожалуйста, попробуйте позже.")

# Команда для добавления меню в канал (только для администраторов)
@dp.message(Command('send_menu'))
async def send_menu_to_channel(message: types.Message):
    try:
        logger.info(f"Получена команда /send_menu от пользователя {message.from_user.id}")
        # Создаем кнопку для канала
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(
                text='Открыть приложение 🚀',
                url='https://t.me/Insight2b_bot/insight2b'
            )
        ]])
        
        # Отправляем сообщение в канал
        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo='https://i.pinimg.com/736x/0d/f2/ec/0df2ec2920cb9276657967121ade978e.jpg',
            caption="🌟 *Добро пожаловать в мир инноваций!*\n\n"
                   "Я — чат бот ПРИЗ\n"
                   "(Практические Решения Изобретательских Задач).\n\n"
                   "ПРИЗ — это инновационный инструмент, который поможет вам:\n"
                   "• Находить креативные решения\n"
                   "• Развивать новые идеи\n"
                   "• Создавать уникальные проекты\n\n"
                   "Нажмите на кнопку ниже, чтобы начать работу с приложением 👇",
            parse_mode="Markdown",
            reply_markup=keyboard
        )
        
        await message.answer("✅ Приветственное сообщение успешно добавлено в канал!")
        logger.info("Успешно отправлено меню в канал")
    except Exception as e:
        logger.error(f"Ошибка в команде /send_menu: {str(e)}")
        await message.answer(f"❌ Ошибка при отправке сообщения в канал: {str(e)}")

async def main():
    try:
        logger.info("Запуск бота...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {str(e)}")

if __name__ == '__main__':
    asyncio.run(main()) 