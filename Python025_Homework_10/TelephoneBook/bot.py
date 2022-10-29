import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import json_module
import csv_module
import txt_module

e_con = ''
e_cur = ''
e_PATH_PROG = ''


def init(conn, cur, PATH_PROG):
    global e_con
    global e_cur
    global e_PATH_PROG
    e_con = conn
    e_cur = cur
    e_PATH_PROG = PATH_PROG


async def exp_csv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    csv_module.exp_db(e_con, e_cur, e_PATH_PROG)
    file1 = open(f'{e_PATH_PROG}/export/export_person.csv', 'rb')
    file2 = open(f'{e_PATH_PROG}/export/export_phones.csv', 'rb')
    file3 = open(f'{e_PATH_PROG}/export/export_types.csv', 'rb')
    await update.message.reply_document(file1)
    await update.message.reply_document(file2)
    await update.message.reply_document(file3)
    file1.close()
    file2.close()
    file3.close()


async def exp_txt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    txt_module.exp_db(e_con, e_cur, e_PATH_PROG)
    file1 = open(f'{e_PATH_PROG}/export/export_person.txt', 'rb')
    file2 = open(f'{e_PATH_PROG}/export/export_phones.txt', 'rb')
    file3 = open(f'{e_PATH_PROG}/export/export_types.txt', 'rb')
    await update.message.reply_document(file1)
    await update.message.reply_document(file2)
    await update.message.reply_document(file3)
    file1.close()
    file2.close()
    file3.close()


async def exp_json(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    json_module.exp_db(e_con, e_cur, e_PATH_PROG)
    file1 = open(f'{e_PATH_PROG}/export/export_person.json', 'rb')
    file2 = open(f'{e_PATH_PROG}/export/export_phones.json', 'rb')
    file3 = open(f'{e_PATH_PROG}/export/export_types.json', 'rb')
    await update.message.reply_document(file1)
    await update.message.reply_document(file2)
    await update.message.reply_document(file3)
    file1.close()
    file2.close()
    file3.close()


async def exp_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Выберете формат для экспорта:\n'
                                    f'json: /exp_json\ncsv:  /exp_csv\ntxt:  /exp_txt')


async def imp_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Загрузите 3 файла(person, phones, types) одного из форматов (json, txt, csv)\n'
                                    f'Затем Выберете команду для импорта в бд\n'
                                    f'json: /imp_json\n'
                                    f'csv:  /imp_csv\n'
                                    f'txt:  /imp_txt\n')


async def imp_csv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    csv_module.imp_db(e_con, e_cur, e_PATH_PROG)
    await update.message.reply_text(f"Файл в формате csv импортирован в базу данных")
    print(f"Файл в формате csv импортирован в базу данных")


async def imp_txt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    txt_module.imp_db(e_con, e_cur, e_PATH_PROG)
    await update.message.reply_text(f"Файл в формате txt импортирован в базу данных")
    print(f"Файл в формате txt импортирован в базу данных")


async def imp_json(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    json_module.imp_db(e_con, e_cur, e_PATH_PROG)
    await update.message.reply_text(f"Файл в формате json импортирован в базу данных")
    print(f"Файл в формате json импортирован в базу данных")


async def Getfile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await (await context.bot.get_file(update.message.document)).download(
        f'{e_PATH_PROG}/import/{update.message.document["file_name"]}')
    await update.message.reply_text(f"File saved as {update.message.document['file_name']}")
    print(f"File saved as {update.message.document['file_name']}")


def bot_start():
    app = ApplicationBuilder().token("token").build()
    app.add_handler(CommandHandler("exp_csv", exp_csv))
    app.add_handler(CommandHandler("exp_txt", exp_txt))
    app.add_handler(CommandHandler("exp_json", exp_json))
    app.add_handler(CommandHandler("export", exp_files))
    app.add_handler(CommandHandler("import", imp_files))
    app.add_handler(CommandHandler("imp_csv", imp_csv))
    app.add_handler(CommandHandler("imp_txt", imp_txt))
    app.add_handler(CommandHandler("imp_json", imp_json))
    app.add_handler(MessageHandler(filters.Document.ALL, Getfile))
    print('Server start')
    app.run_polling()
