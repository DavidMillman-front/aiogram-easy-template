from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram import types

async def options_to_read(lang, message: types.Message):

    Juz = {
        'uzl': "Juzlar",
        'uzk': "Жузлар",
        'ru': "Жузи",
        'en': "Juzs"
    }
    Surah = {
        'uzl': "Suralar",
        'uzk': "Суралар",
        'ru': "Суры",
        'en': "Surahs"
    }
    main_menu = {
        'uzl': "Asosiy menu",
        'uzk': "Асосий меню",
        'ru': "Главное меню",
        'en': "Main menu"
    }
    text = {
        'uzl': "Davom etish uchun pastdagi tugmalardan birini tanlang!",
        'uzk': "Давом этиш учун пастдаги тугмалардан бирини танланг!",
        'ru': "Выберите одну из кнопок ниже, чтобы продолжить!",
        'en': "Press a button below to continue!"
    }

    options_to_read = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder=text[lang], one_time_keyboard=True)
    options_to_read.add(KeyboardButton(text=Juz[lang]), KeyboardButton(text=Surah[lang]),
                        KeyboardButton(text=main_menu[lang]))
    return options_to_read
