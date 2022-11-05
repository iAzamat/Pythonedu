import telebot
# pip install simpleeval
from simpleeval import simple_eval
import logger

bot = telebot.TeleBot("token")

value = ""
old_value = ""

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton("C", callback_data="C"),
             telebot.types.InlineKeyboardButton("<==", callback_data="backspace"))

keyboard.row(telebot.types.InlineKeyboardButton("j", callback_data="j"),
             telebot.types.InlineKeyboardButton("(", callback_data="("),
             telebot.types.InlineKeyboardButton(")", callback_data=")"),
             telebot.types.InlineKeyboardButton("/", callback_data=" / "))

keyboard.row(telebot.types.InlineKeyboardButton("7", callback_data="7"),
             telebot.types.InlineKeyboardButton("8", callback_data="8"),
             telebot.types.InlineKeyboardButton("9", callback_data="9"),
             telebot.types.InlineKeyboardButton("*", callback_data=" * "))

keyboard.row(telebot.types.InlineKeyboardButton("4", callback_data="4"),
             telebot.types.InlineKeyboardButton("5", callback_data="5"),
             telebot.types.InlineKeyboardButton("6", callback_data="6"),
             telebot.types.InlineKeyboardButton("-", callback_data=" - "))

keyboard.row(telebot.types.InlineKeyboardButton("1", callback_data="1"),
             telebot.types.InlineKeyboardButton("2", callback_data="2"),
             telebot.types.InlineKeyboardButton("3", callback_data="3"),
             telebot.types.InlineKeyboardButton("+", callback_data=" + "))

keyboard.row(telebot.types.InlineKeyboardButton(" ", callback_data="no"),
             telebot.types.InlineKeyboardButton("0", callback_data="0"),
             telebot.types.InlineKeyboardButton(",", callback_data="."),
             telebot.types.InlineKeyboardButton("=", callback_data="="))


@bot.message_handler(commands=["calc"])
def getmessage(message):
    global value
    if value == "":
        bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@bot.message_handler(commands=["log"])
def getlog(message):
    doc = open('log/log.csv', 'rb')
    bot.send_document(message.from_user.id, doc)


@bot.message_handler(commands=["start", "help", "помощь"])
def gethelp(message):
    bot.send_message(message.chat.id, 'Калькулятор для вычисления комплексных и рациональных чисел\n'
                                      'Комплексные числа рекомендуется задавать в виде: (1+5j)\n'
                                      'Для запуска калькулятора введите команду: /calc\n'
                                      'Для получения логов используйте команду: /log')


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == "no":
        pass
    elif data == "backspace":
        value = value[:-1]
    elif data == "C":
        value = ""
    elif data == "j":
        if len(value) == 0:
            value = '1j'
        else:
            value = value + 'j'
    elif data == "=":
        try:
            value = value.replace('+ j', '+ 1j').replace('- j', '- 1j')
            prew_result = value
            value = str(simple_eval(value))
            result = value
            log_str = f'{prew_result} = {result}'
            logger.log_operation(log_str)
        except:
            value = "Ошибка!"
    else:
        value += data

    if value != old_value:
        if value == "":
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="0",
                                  reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value,
                                  reply_markup=keyboard)

    old_value = value
    if value == "Ошибка!":
        value = ""


print('Server started')
bot.polling(none_stop=False, interval=0)
