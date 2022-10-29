from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

data = []

LASTNAME, FIRSTNAME, PATRONYMIC, NOTE, NUMBER, NUMBER_TYPE = range(6)


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
    await update.message.reply_text("Введите номер телефона")
    return NUMBER


async def skip_note(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    text = ''
    data.append(text)
    await update.message.reply_text("Введите номер телефона")
    return NUMBER


async def telnumber(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    await update.message.reply_text("Введите тип телефона")
    return NUMBER_TYPE


async def teltype(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    data.append(update.message.text)
    await update.message.reply_text("Добавляем в базу данных")
    print(data)
    # отправка в бд
    data.clear()
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    await update.message.reply_text(
        "Вы отменили операцию", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def main() -> None:
    application = Application.builder().token("token").build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("addcontact", addcontact)],
        states={
            LASTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, lastname)],
            FIRSTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, firstname)],
            PATRONYMIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, patronymic)],
            NOTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, note), CommandHandler("skip", skip_note)],
            NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, telnumber)],
            NUMBER_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, teltype)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
