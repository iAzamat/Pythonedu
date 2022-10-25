'''
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

my_token = ""

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global candies
    candies = 100
    await update.message.reply_text(f'На столе {candies} конфет, ваш ход')


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global candies
    msg = update.message.text
    candies -= int(msg)
    await update.message.reply_text(f'На столе {candies} конфет')
    if win_in_game():
        await update.message.reply_text(f'Выиграл {update.effective_user.first_name}')
        return
    await update.message.reply_text(f'Бот взял {bot_candy()} конфет, на столе {candies} конфет')
    if win_in_game():
        await update.message.reply_text('Выиграл БОТ')
        return


def bot_candy():
    global candies
    if candies > 28:
        candy = candies % 29
    else:
        candy = candies
    candies -= candy
    return candy


def win_in_game():
    global candies
    return candies < 1


candies = 100

app = ApplicationBuilder().token(my_token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", new_game))
app.add_handler(MessageHandler(filters.TEXT, game))

app.run_polling()
