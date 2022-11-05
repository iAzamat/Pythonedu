import sqlite3
import bot

# PATH_PROG = 'd:/GDisk/GeekBraims/Python/PythonSeminars/Seminar7/PhoneBook'
PATH_PROG = ''

conn = sqlite3.connect(f'{PATH_PROG}/db/phone_book.db')
cur = conn.cursor()

bot.init(conn, cur, PATH_PROG)
bot.bot_start()
