import logging
import time
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import callback_query
from keyboards.inline.choose_language import create_choosing_language_kb
from states.language_state import Language
from loader import dp, bot
from keyboards.default.List_of_books_kb import list_of_books

delete = bool

# used data forms
# data['language']


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    f = open("ids.txt", "a")
    user_id = ','+str(message.chat.id)
    f.write(user_id)
    f.close()
    id = message.message_id
    await bot.delete_message(chat_id=message.chat.id, message_id=id)
    greeting_message = f"""Assalomu alaykum, {message.from_user.full_name}. Bu yerda siz Qur'on kitobini o'qish uchun 
    barcha yo'llardan osonlikcha foydalanishingiz mumkin. Davom etish uchun iltimos tilni tanlang!\n\nAссалому 
    алайкум, {message.from_user.full_name}. Здесь вы можете легко использовать все способы чтения книги Корана. 
    Пожалуйста, выберите язык для продолжения! \n\n Assalomu alaykum, {message.from_user.full_name}. Here you can 
    easily use all the ways to read the Quran. Please choose a
    language to continue!"""
    await message.answer(text=greeting_message, reply_markup=create_choosing_language_kb)
    await Language.Choosing_language.set()


@dp.callback_query_handler(state=Language.Choosing_language)
async def change_interface_language(call: callback_query.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['language'] = str(call.data)
    lang_changed = {
        "uzl":"Interfeys o'zbekchaga o'zgartirildi.",
        "uzk":"Интерфейс ўзбекчага ўзгартирилди.",
        "ru":"Интерфейс изменен на русский.",
        "en":"Interface was changed into English."
    }
    await call.message.reply(text=lang_changed[call.data])
    time.sleep(3)
    id = call.message.message_id+1
    await call.message.delete()
    await call.bot.delete_message(chat_id=call.message.chat.id, message_id=id)
    await choose_books(call.message, state)
    await Language.Choosing_book.set()


async def choose_books(message: types.Message, state: FSMContext):
    global delete
    async with state.proxy() as data:
        lang = data['language']
    choose_books_text = {
        'uzl': "O'qimoqchi bo'lgan kitobingizni tanlang!",
        'uzk': "Ўқимоқчи бўлган китобингизни танланг!",
        'ru': "Выберите книгу, которую хотите прочитать!",
        'en': "Choose the book you want to read!"
    }
    await message.answer(text=choose_books_text[lang], reply_markup=await list_of_books(state))
    delete = True

@dp.message_handler(state='*', commands='changelang')
@dp.message_handler(Text(equals='changelang', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        lang = data['language']
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    choose_lang = {
        "uzl":"Tilni tanlang!",
        "uzk":"Тилни танланг!",
        "ru":"Выберите язык ниже",
        "en":"Choose the language below!"
    }
    await message.answer(text=choose_lang[lang], reply_markup=create_choosing_language_kb)
    await Language.Choosing_language.set()

