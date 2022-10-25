# Задача 2. Прикрутить бота к задачам с предыдущего семинара:
#   2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

from new_person import writing_down as wd
import view

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

t_book = wd()
view.export_book(t_book)

async def add_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # не доработана функция
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def list_telephone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open('newfile.txt', 'rb')
    await update.message.reply_document(file)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("token").build()

app.add_handler(CommandHandler("add", add_list)) # не доработана функция
app.add_handler(CommandHandler("list", list_telephone))
app.add_handler(CommandHandler("hello", hello))



app.run_polling()

