from aiogram import Dispatcher

from handlers import anketa, start

def include_routers(db: Dispatcher):
    db.include_routers(
        start.router,
        anketa.router
    )