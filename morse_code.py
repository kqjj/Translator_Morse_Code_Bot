from aiogram import Bot, types
from logging import disable
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config

bot = Bot(token=config.TOKEN) #Ваш токен
dp = Dispatcher(bot)

Letters = {
      'а': '•−','А': '•−',
      'б': '−•••','Б': '−•••',
      'в': '•−−','В': '•−−',
      'г': '••••','Г': '••••',
      'ґ': '−−•','Ґ': '−−•',
      'д': '−••','Д': '−••',
      'е': '•','Е': '•',
      'є': '••−••','Є': '••−••',
      'ж': '•••−','Ж': '•••−',
      'з': '−−••','З': '−−••',
      'и': '−•−−','И': '−•−−',
      'і': '••','І': '••',
      'ї': '•−−−•','Ї': '•−−−•',
      'й': '•−−−','Й': '•−−−',
      'к': '−•−','К': '−•−',
      'л': '•−••','Л': '•−••',
      'м': '−−','М': '−−',
      'н': '−•','Н': '−•',
      'о': '−−−','О': '−−−',
      'п': '•−−•','П': '•−−•',
      'р': '•−•','Р': '•−•',
      'с': '•••','С': '•••',
      'т': '−','Т': '−',
      'у': '••−','У': '••−',
      'ф': '••−•','Ф': '••−•',
      'х': '−−−−','Х': '−−−−',
      'ц': '−•−•','Ц': '−•−•',
      'ч': '−−−•','Ч': '−−−•',
      'ш': '−−•−','Ш': '−−•−',
      'щ': '−−•−−','Щ': '−−•−−',
      'ь': '−••−','Ь': '−••−',
      'ю': '••−−','Ю': '••−−',
      'я': '•−•−','Я': '•−•−',
      '1': '•−−−−','2': '••−−−',
      '3': '•••−−','4': '••••−',
      '5': '•••••','6': '−••••',
      '7': '−−•••','8': '−−−••',
      '9': '−−−−•','0': '−−−−−',
      '?': '••−−••','!': '−−••−−',
      '.': '••••••',',': '•−•−•−',
      '+': '−••••−','-': '•−•−•'  
}

@dp.message_handler(commands=['start'])
async def cmd_answer(message: types.Message):
      await message.answer('<b>👋 Привіт, я Перекладач Азбуки Морзе 💬</b>\n<b>🇺🇦 Перекладаю з Української Мови на Азбуку Морзе ⚙️</b>\n\n<b>📋 Таблиця кодування</b> - /table\n<b>📚 Перекласти</b> - /translate\n<code> - Наприклад: /translate Перемога</code>\n<b>⁉️ Технічна підтримка</b> - /help', parse_mode='HTML')
      
@dp.message_handler(commands=['help'])
async def cmd_answer(message: types.Message):
      await message.answer('⁉️<b> Якщо у вас є проблеми.</b> \n✉️ <b>Напишіть мені</b> <a href="https://t.me/nikit0ns">@nikitons</a><b>.</b>', disable_web_page_preview=True, parse_mode='HTML')

@dp.message_handler(commands=['table'])
async def cmd_answer(message: types.Message):
      await message.answer('<b>📋 Це таблиця Азбуки Морзе.</b>', parse_mode='HTML')
      await dp.bot.send_photo(chat_id=message.from_user.id, photo='AgACAgIAAxkBAAIBf2Mp5o1CjXwpYjpRGlL2NySw0AH-AAL4wTEb8vpQSZYmRkqjqdK7AQADAgADcwADKQQ')


@dp.message_handler(commands=['translate'])
async def cmd_answer(message: types.Message):
      await message.answer("".join(map(lambda x: Letters[x.lower()] if x in Letters else x, message.get_args())), parse_mode='HTML')
      
if __name__ == '__main__':
      executor.start_polling(dp)