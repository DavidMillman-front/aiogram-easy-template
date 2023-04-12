from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back = {
    "uzl": "Ortga⬅️",
    "uzk": "Ортга⬅️",
    "ru": "Назад⬅️",
    "en": "Go back⬅️️"
}

main_menu = {
    'uzl': "Asosiy menu",
    'uzk': "Асосий меню",
    'ru': "Главное меню",
    'en': "Main menu"
}
another = {
    "uzl": f"Boshqa juz!",
    "uzk": f"Бошқа жуз!",
    "ru": f"Другой жуз!",
    "en": f"Another juz!"
}
async def getting_list_of_juzs(lang):
    text = {
        "uzl": "Juzlar ro'yhatini olish!",
        "uzk": "Жузлар рўйҳатини олиш!",
    "ru": "Получить список жузи!",
    "en": "Get the list of juzs"
    }

    ikb = InlineKeyboardMarkup()
    ikb.insert(InlineKeyboardButton(text=text[lang], callback_data="list-of-juzs"))
    ikb.insert(InlineKeyboardButton(text=back[lang], callback_data='back-juz'))
    return ikb

def kb_juz_option_to_continue(rem_ayahs, lang):
    next_ayahs = {
        "uzl": f"Keyingi {rem_ayahs} ta oyat➡️",
        "uzk": f"Кейинги {rem_ayahs} та оят➡️",
        "ru": f"Cледушие {rem_ayahs} аяти➡️",
        "en": f"Next {rem_ayahs} ayahs➡️"
    }
    ikb= InlineKeyboardMarkup(row_width=2)
    ikb.insert(InlineKeyboardButton(text=next_ayahs[lang], callback_data="next-ayahs-juz"))
    ikb.insert(InlineKeyboardButton(text=another[lang], callback_data="calling-juz"))
    ikb.insert(InlineKeyboardButton(text=back[lang], callback_data="back-juz"))
    ikb.insert(InlineKeyboardButton(text=main_menu[lang], callback_data="main-menu"))
    return ikb

def kb_endOfJuz(lang):
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.insert(InlineKeyboardButton(text=another[lang], callback_data="calling-juz"))
    ikb.insert(InlineKeyboardButton(text=back[lang], callback_data="back-juz"))
    ikb.insert(InlineKeyboardButton(text=main_menu[lang], callback_data="main-menu"))
    return ikb