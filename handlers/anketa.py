from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states.anketa import Anketa
from keyboards.anketa import *

router = Router()

@router.message(Command("anketa"))
async def anketa_handler(msg: Message, state: FSMContext):
    await state.set_state(Anketa.name)
    await msg

    