from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.default.List_of_books_kb import list_of_books
from keyboards.default.options_for_Quran import options_to_read
from keyboards.inline.kb_for_juzs import getting_list_of_juzs
from keyboards.inline.kb_for_surahs import getting_list_of_surahs
from .start import choose_books
from states.states_for_Quran import states_for_Quran
from states.language_state import Language
from .start import delete

from keyboards.inline.kb_for_Quran import going_back_to_Quran_options




@dp.message_handler(state=Language.Choosing_book)
async def quran_cmd(message: types.Message, state: FSMContext):
    global delete
    if delete:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
        delete = not delete


    await message.delete()
    text = {
        'uzl': "Qur'onni ikki xil uslubda o'qishingiz mumkin. Ikkalasidan birini tanglang!",
        'uzk': "Қуръонни икки хил услубда ўқишингиз мумкин. Иккаласидан бирини тангланг!",
        'ru': "Вы можете читать Коран двумя разными способами. Выберите один из двух!",
        'en': "You can read Quran in two ways. Please choose one!"
    }
    async with state.proxy() as data:
        lang = data['language']
        print(lang)
    # await message.delete()
    await message.answer(text[lang], reply_markup=await options_to_read(lang, message))
    await states_for_Quran.option.set()



@dp.message_handler(state=states_for_Quran.option)
async def option_to_read_cmd(message: types.Message, state: FSMContext):
    global delete
    await message.delete()


    async with state.proxy() as data:
        lang = data['language']
        data['latest-ayah'] = 1
        data['latest-ayah-juz'] = 1
    text = message.text
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
    if text in Juz[lang]:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
        kb = await getting_list_of_juzs(lang)
        kb.insert(await going_back_to_Quran_options(lang))
        text = {
            'uzl': "Juz raqamini kiriting! Yoki pastdagi tugmani bosing!",
            'uzk': "Жуз рақамини киритинг! Ёки пастдаги тугмани босинг!",
            'ru': "Введите номер жуза! Или нажмите кнопку ниже!",
            'en': "Enter the number of juz. Or click the button below"
        }
        await message.answer(text=text[lang], reply_markup=await getting_list_of_juzs(lang))
        await states_for_Quran.juz.set()
    elif text in Surah[lang]:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)

        text = {
            'uzl': "Sura raqamini kiriting! Yoki pastdagi tugmani bosing!",
            'uzk': "Сура рақамини киритинг! Ёки пастдаги тугмани босинг!",
            'ru': "Введите номер cура! Или нажмите кнопку ниже!",
            'en': "Enter the number of surah. Or click the button below"
        }
        await message.answer(text=text[lang], reply_markup=await getting_list_of_surahs(lang))
        await states_for_Quran.surah.set()
    elif text in main_menu[lang]:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)

        delete = True
        await Language.Choosing_book.set()
        await choose_books(message, state)


