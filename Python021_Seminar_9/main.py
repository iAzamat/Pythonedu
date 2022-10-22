'''
## Групповая работа [2]
Учимся настраивать виртуальное окружение и работать с [PIP](https://pypi.org/)
В качестве пробы библиотек к программам предыдущего модуля подключить работу с XML\SON
Для тренировки можно создания телеграм-бота полезные ссылки:

https://core.telegram.org/bots
https://github.com/python-telegram-bot/python-telegram-bot

**Задача:** при помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:
1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
2. Создайте программу для игры с конфетами человек против человека.
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
    Все конфеты оппонента достаются сделавшему последний ход.
    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    a) Добавьте игру против бота.
    b) Подумайте как наделить бота "интеллектом"
'''

my_token = ''

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import candy_game

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def remove_abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    my_list = list(filter(lambda x: 'абв' not in x, msg.split()))
    await update.message.reply_text(' '.join(my_list))


app = ApplicationBuilder().token(my_token).build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT, remove_abc))

print('Server started')
app.run_polling()

#================================================



