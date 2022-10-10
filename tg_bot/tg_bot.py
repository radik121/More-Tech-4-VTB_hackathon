from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiohttp import ClientSession
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import json
from conf import TG_API

bot = Bot(token=TG_API, parse_mode='HTML')

dp = Dispatcher(bot)

positions = []
positions_dict = {
    'Бухгалтер': 'buhgalter',
    'Ген. Директор': 'gendir',
}


@dp.message_handler(Text(equals='Показать 2-3 новости'))
@dp.message_handler(Text(equals='Показать все новости'))
async def get_news(message: types.Message):
    headers = {
        'Content-Type': 'application/json'
    }
    data = None
    position = positions_dict[positions[0]]
    async with ClientSession() as session:
        try:
            if message.text == 'Показать 2-3 новости':
                response = await session.get(f'http://localhost:8000/apiv1/show2_3/{position}/')
            elif message.text == 'Показать все новости':
                response = await session.get(f'http://localhost:8000/apiv1/all/{position}/')
            data = await response.json()
        except Exception as ex:
            print(ex)
            await message.answer(text='Произошла ошибка. \n' 'Попробуйте снова.')
    # data = {
    #     1: {
    #         'title': 'Заголовок',
    #         'description': 'Краткое описание',
    #         'url': 'Ссылка',
    #         'date': 'Дата',
    #         'trends': 'Тренды',
    #         'insites': 'Инсайты'
    #     }
    # }
    if data is not None:
        for item in data:
            news_message = f'{hlink(item.get("title"), item.get("url"))}\n' \
                           f'Краткое описание: {hbold(item.get("description"))}\n' \
                           f'Дата: {hbold(item.get("date"))}\n' \
                           f'Тренды: {hbold(item.get("trends"))}\n' \
                           f'Инсайты: {hbold(item.get("insites"))}'
            await message.answer(text=news_message)
    await message.answer(text='Выберите следующее действие:')


@dp.message_handler(commands=['start'])
@dp.message_handler(Text(equals='Сменить должность'))
async def start_bot(message: types.Message):
    start_buttons = ['Бухгалтер', 'Ген. Директор']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer(text='Выберите вашу должность', reply_markup=keyboard)


@dp.message_handler()
async def count_news(message: types.Message):
    start_buttons = ['Показать 2-3 новости', 'Показать все новости', 'Сменить должность']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    if positions:
        positions.clear()
    positions.append(message.text)
    await message.answer(text='Выберите следующее действие', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
