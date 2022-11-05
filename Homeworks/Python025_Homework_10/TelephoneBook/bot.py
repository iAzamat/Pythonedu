from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import \
    ApplicationBuilder, \
    CommandHandler, \
    MessageHandler, \
    ContextTypes, \
    filters, \
    ConversationHandler

import json_module
import csv_module
import txt_module
import functools
import operator

e_PATH_PROG = ''
data = []
IDA, LASTNAME, FIRSTNAME, PATRONYMIC, NOTE, NUMBER, NUMBER_TYPE = range(7)


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
    reply_keyboard = [["/exp_json", "/exp_csv", "/exp_txt"]]
    await update.message.reply_text(f'Выберете формат для экспорта:', reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True,
        input_field_placeholder=f'Выберете формат для экспорта:'), )


async def imp_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["/imp_json", "/imp_csv", "/imp_txt"]]
    await update.message.reply_text(
        f'Загрузите 3 файла(person, phones, types) одного из форматов (json, txt, csv)\n'
        f'Затем выберете команду для импорта в бд\n',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True,
            input_field_placeholder="Выберете команду для импорта в бд\n"), )


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


# ======================= /addcontact ==================================================================================
async def addcontact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Введите фамилию:")
    return LASTNAME


async def lastname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    await update.message.reply_text("Введите имя:")
    return FIRSTNAME


async def firstname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    await update.message.reply_text("Введите отчество:")
    return PATRONYMIC


async def patronymic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    await update.message.reply_text("Введите заметку: Пропустить /skip")
    return NOTE


async def note(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    await update.message.reply_text("Добавляем в базу данных")
    if len(data) == 4:
        exec_str = 'SELECT max(id_person)+1 FROM Persons'
        e_cur.execute(exec_str)
        new_id = functools.reduce(operator.add, (e_cur.fetchone()))
        lastname_db = data[0]
        firstname_db = data[1]
        patronymic_db = data[2]
        note_db = data[3]
        exec_str = f'REPLACE INTO persons (id_person, lastname, firstname, patronymic, note) VALUES ({new_id}, ' \
                   f'"{lastname_db}", "{firstname_db}", "{patronymic_db}", "{note_db}")'
        e_cur.execute(exec_str)
        e_con.commit()
    elif len(data) == 5:
        new_id = data[0]
        lastname_db = data[1]
        firstname_db = data[2]
        patronymic_db = data[3]
        note_db = data[4]
        exec_str = f'REPLACE INTO persons (id_person, lastname, firstname, patronymic, note) VALUES ({new_id}, ' \
                   f'"{lastname_db}", "{firstname_db}", "{patronymic_db}", "{note_db}")'
        e_cur.execute(exec_str)
        e_con.commit()
    data.clear()
    return ConversationHandler.END


async def skip_note(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    text = None
    data.append(text)
    await update.message.reply_text("Добавляем в базу данных")
    if len(data) == 4:
        exec_str = 'SELECT max(id_person)+1 FROM Persons'
        e_cur.execute(exec_str)
        new_id = functools.reduce(operator.add, (e_cur.fetchone()))
        lastname_db = data[0]
        firstname_db = data[1]
        patronymic_db = data[2]
        note_db = data[3]
        exec_str = f'REPLACE INTO persons (id_person, lastname, firstname, patronymic, note) VALUES ({new_id}, ' \
                   f'"{lastname_db}", "{firstname_db}", "{patronymic_db}", "{note_db}")'
        e_cur.execute(exec_str)
        e_con.commit()
    elif len(data) == 5:
        new_id = data[0]
        lastname_db = data[1]
        firstname_db = data[2]
        patronymic_db = data[3]
        note_db = data[4]
        exec_str = f'REPLACE INTO persons (id_person, lastname, firstname, patronymic, note) VALUES ({new_id}, ' \
                   f'"{lastname_db}", "{firstname_db}", "{patronymic_db}", "{note_db}")'
        e_cur.execute(exec_str)
        e_con.commit()
    data.clear()
    return ConversationHandler.END


# =========================== /delcontact ==============================================================================
async def delcontact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    e_cur.execute(f"select * from persons;")
    list_persons = e_cur.fetchall()
    text = ''
    await update.message.reply_text("Список для удаления:")

    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id пользователя /cancel отмена")
    return IDA


async def id_del(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    exec_str = f'DELETE from persons  WHERE id_person = {data[0]}'
    e_cur.execute(exec_str)
    e_con.commit()
    exec_str = f'DELETE from phones  WHERE id_person = {data[0]}'
    e_cur.execute(exec_str)
    e_con.commit()

    await update.message.reply_text(f'Пользователь с id: {data[0]} удален')
    data.clear()
    return ConversationHandler.END


# ============================= /modcontact ============================================================================
async def modcontact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    e_cur.execute(f"select * from persons;")
    list_persons = e_cur.fetchall()
    text = ''
    await update.message.reply_text(f"Список для изменения:")

    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id пользователя")
    return IDA


async def id_mod(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    await update.message.reply_text(f'Пользователь с id: {data[0]} выбран для изменения /cancel - отмена')
    await update.message.reply_text("Введите фамилию:")
    return LASTNAME


# ============================= /addtype ===============================================================================
async def addtype(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Введите название типа")
    return IDA


async def id_type_add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    if len(data) == 1:
        exec_str = 'SELECT max(id_type)+1 FROM types'
        e_cur.execute(exec_str)
        new_id = functools.reduce(operator.add, (e_cur.fetchone()))
        type_phone = data[0]
        exec_str = f'REPLACE INTO types (id_type, c_type) VALUES ({new_id}, "{type_phone}")'
        e_cur.execute(exec_str)
        e_con.commit()
    elif len(data) == 2:
        new_id = data[0]
        type_phone = data[1]
        exec_str = f'REPLACE INTO types (id_type, c_type) VALUES ({new_id}, "{type_phone}")'
        e_cur.execute(exec_str)
        e_con.commit()
    await update.message.reply_text(f'Название типа: {data[0]} добавлено\\изменено')
    data.clear()
    return ConversationHandler.END


# ============================= /deltype ===============================================================================
async def deltype(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    e_cur.execute(f"select * from types;")
    list_persons = e_cur.fetchall()
    text = ''
    await update.message.reply_text(f"Список для удаления /cancel - отмена:")

    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id типа")
    return IDA


async def id_type_del(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    exec_str = f'DELETE from types  WHERE id_type = {data[0]}'
    e_cur.execute(exec_str)
    e_con.commit()
    await update.message.reply_text(f'Название типа: {data[0]} удалено')
    data.clear()
    return ConversationHandler.END


# ============================= /modtype ===============================================================================
async def modtype(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    e_cur.execute(f"select * from types;")
    list_persons = e_cur.fetchall()
    text = ''
    await update.message.reply_text(f"Список для изменения:")

    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id типа")
    return IDA


async def id_type_mod(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    # изменения типа в бд data[1] c индексом data[0]
    await update.message.reply_text(f'Название типа: {data[0]} выбрано для изменения')
    await update.message.reply_text("Введите название типа")
    return LASTNAME


# ============================= /addphone ==============================================================================
async def addphone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    e_cur.execute(f"select * from persons;")
    list_persons = e_cur.fetchall()
    text = ''
    await update.message.reply_text(f"Список контактов:")

    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id контакта:")
    return LASTNAME


async def addphoneid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    await update.message.reply_text("Введите телефонный номер:")
    return FIRSTNAME


async def addphonenumber(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # показать список типов телефонов
    user = update.message.from_user
    data.append(update.message.text)
    e_cur.execute(f"select * from types;")
    list_persons = e_cur.fetchall()
    text = ''
    await update.message.reply_text(f"Список типов телефонов:")

    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id типа:")
    return PATRONYMIC


async def addphonetype(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)

    if len(data) == 3:
        exec_str = 'SELECT max(id_phone)+1 FROM phones'
        e_cur.execute(exec_str)
        new_id = functools.reduce(operator.add, (e_cur.fetchone()))
        id_person = data[0]
        id_type = data[2]
        phone_number = data[1]
        exec_str = f'REPLACE INTO phones (id_phone, id_person, id_type, phone_number) VALUES ' \
                   f'({new_id}, "{id_person}", "{id_type}" , "{phone_number}")'
        e_cur.execute(exec_str)
        e_con.commit()

    await update.message.reply_text("Добавляем в базу данных")
    # отправка в бд на добавление или изменение, в зависимости от размера data[]
    data.clear()
    return ConversationHandler.END


# ============================= /delphone ==============================================================================
async def delphone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    e_cur.execute(f"select * from persons;")
    list_persons = e_cur.fetchall()
    text = ''
    await update.message.reply_text(f"Список контактов:")

    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id контакта")
    return IDA


async def delphone_id_person(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    e_cur.execute(f"select id_phone, phone_number, c_type  from v_full WHERE id_person={data[0]};")
    list_persons = e_cur.fetchall()
    text = ''
    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text("Список телефонов этого ID")
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id телефона:")
    return LASTNAME


async def id_phone_del(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    exec_str = f'DELETE from phones  WHERE (id_phone = {data[1]} and id_person = {data[0]})'
    e_cur.execute(exec_str)
    e_con.commit()
    await update.message.reply_text(f'Телефон с ID:{data[1]} удален из базы данных')
    data.clear()
    return ConversationHandler.END


# ============================= /modphone ==============================================================================
async def modphone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    e_cur.execute(f"select * from persons;")
    list_persons = e_cur.fetchall()
    text = ''
    await update.message.reply_text(f"Список контактов:")

    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id контакта:")
    return IDA


async def modphone_id_person(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # показать список телефоном с этим ID
    user = update.message.from_user
    data.append(update.message.text)
    e_cur.execute(f"select id_phone, phone_number, c_type  from v_full WHERE id_person={data[0]};")
    list_persons = e_cur.fetchall()
    text = ''
    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text("Список телефонов этого ID")
    await update.message.reply_text(text)
    await update.message.reply_text("Введите id телефона:")
    return LASTNAME


async def modphone_id_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    await update.message.reply_text("Введите номер телефона:")
    return FIRSTNAME


async def modphone_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    e_cur.execute(f"select * from types;")
    list_persons = e_cur.fetchall()
    text = ''

    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text(text)
    await update.message.reply_text("Введите ID типа телефона:")
    return PATRONYMIC


async def modphone_id_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)

    if len(data) == 4:
        id_person = data[0]
        new_id = data[1]
        phone_number = data[2]
        id_type = data[3]
        exec_str = f'REPLACE INTO phones (id_phone, id_person, id_type, phone_number) VALUES ' \
                   f'({new_id}, "{id_person}", "{id_type}" , "{phone_number}")'
        e_cur.execute(exec_str)
        e_con.commit()

    await update.message.reply_text("Данные изменены в базе данных:")
    data.clear()
    return ConversationHandler.END


# ============================= /showall ===============================================================================
async def showall(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    e_cur.execute(f"select id_person, lastname, firstname, patronymic, note, phone_number, c_type  from v_full;")
    list_persons = e_cur.fetchall()
    text = ''
    for elem in list_persons:
        for index in range(len(elem)):
            text += str(elem[index]) + " "
        text += '\n'
    await update.message.reply_text("Список контактов:")
    await update.message.reply_text(text)

    return IDA


# ============================= /showpersoninfo ========================================================================
async def showpersoninfo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # показать список телефоном с этим ID
    user = update.message.from_user
    data.append(update.message.text)
    e_cur.execute(f"select phone_number, c_type  from v_full WHERE id_person={data[0]};")
    list_persons = e_cur.fetchall()
    text = ''
    await update.message.reply_text("Список телефонов этого ID c типами")
    if len(list_persons) > 0:
        for elem in list_persons:
            for index in range(len(elem)):
                text += str(elem[index]) + " "
            text += '\n'
        await update.message.reply_text(text)
    data.clear()
    return ConversationHandler.END


# ======================================================================================================================


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    await update.message.reply_text(
        "Вы отменили операцию", reply_markup=ReplyKeyboardRemove()
    )
    data.clear()
    return ConversationHandler.END


# ======================================================================================================================

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Список команд:")
    text = 'Импорт: /import \n' \
           'Экспорт: /export\n' \
           'Добавить\\Изменить\\Удалить контакт:\n/addcontact\t /modcontact\t /delcontact\n' \
           'Добавить\\Изменить\\Удалить номер телефона:\n/addphone\t /modphone\t /delphone\n' \
           'Добавить\\Изменить\\Удалить тип телефона:\n/addtype\t /modtype\t /deltype\n' \
           'Показать телефонный справочник /showall\n' \
           'Показать визитную карточку контакта: /showpersoninfo\n' \
           'Отмена операций: /cancel'
    await update.message.reply_text(text)


# ======================================================================================================================
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
    app.add_handler(CommandHandler("showall", showall))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(MessageHandler(filters.Document.ALL, Getfile))

    # ==========================================================
    conv_handler1 = ConversationHandler(
        entry_points=[CommandHandler("addcontact", addcontact)],
        states={
            LASTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, lastname)],
            FIRSTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, firstname)],
            PATRONYMIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, patronymic)],
            NOTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, note), CommandHandler("skip", skip_note)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler1)
    # ==========================================================
    conv_handler2 = ConversationHandler(
        entry_points=[CommandHandler("delcontact", delcontact)],
        states={
            IDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, id_del)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler2)
    # ==========================================================
    conv_handler3 = ConversationHandler(
        entry_points=[CommandHandler("modcontact", modcontact)],
        states={
            IDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, id_mod)],
            LASTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, lastname)],
            FIRSTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, firstname)],
            PATRONYMIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, patronymic)],
            NOTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, note), CommandHandler("skip", skip_note)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler3)
    # ==========================================================
    conv_handler4 = ConversationHandler(
        entry_points=[CommandHandler("addtype", addtype)],
        states={
            IDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, id_type_add)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler4)

    # ==========================================================
    conv_handler5 = ConversationHandler(
        entry_points=[CommandHandler("deltype", deltype)],
        states={
            IDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, id_type_del)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler5)

    # ==========================================================
    conv_handler6 = ConversationHandler(
        entry_points=[CommandHandler("modtype", modtype)],
        states={
            IDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, id_type_mod)],
            LASTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, id_type_add)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler6)
    # ==========================================================
    conv_handler7 = ConversationHandler(
        entry_points=[CommandHandler("addphone", addphone)],
        states={
            LASTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, addphoneid)],
            FIRSTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, addphonenumber)],
            PATRONYMIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, addphonetype)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler7)
    # ==========================================================
    conv_handler8 = ConversationHandler(
        entry_points=[CommandHandler("delphone", delphone)],
        states={
            IDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, delphone_id_person)],
            LASTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, id_phone_del)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler8)
    # ==========================================================
    conv_handler9 = ConversationHandler(
        entry_points=[CommandHandler("modphone", modphone)],
        states={
            IDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, modphone_id_person)],
            LASTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, modphone_id_phone)],
            FIRSTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, modphone_phone_number)],
            PATRONYMIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, modphone_id_type)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler9)

    conv_handler10 = ConversationHandler(
        entry_points=[CommandHandler("showpersoninfo", modphone)],
        states={
            IDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, showpersoninfo)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler10)

    print('Server start')
    app.run_polling()
