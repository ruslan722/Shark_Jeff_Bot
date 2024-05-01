import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, \
    keyboard_button, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

bot =Bot(token="7088407944:AAEj6aTi2xMD1BlCan6k8UTSP3cRKFhv2Eo")
db =Dispatcher()
router =Router()



class Anketa(StatesGroup):
    name = State()
    age = State()
    gender = State()


@router.message(Command("anketa"))
async def anketa_handler(msg: Message, state: FSMContext):
    await state.set_state(Anketa.name)
    markup= InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Отмена", callback_data="cancel_anketa")]])
    await msg.answer("Введите ваше имя", reply_markup=markup)

@router.callback_query(F.data == 'cancel_anketa')
async def cancel_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.aswer("Регистрация отменена")

@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Назад', callback_data='set_name_anketa'),
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])
    await msg.answer('Введите ваш возраст', reply_markup=markup)

@router.callback_query(F.data =='set_name_anketa')
async def set_name_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    await anketa_handler(callback_query.message, state)

@router.message(Anketa.age)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer('')
