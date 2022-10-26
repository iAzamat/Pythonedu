from tkinter import *
from tkinter import ttk
import sqlite3
import functools 
import operator


conn = sqlite3.connect('db\phone_book.db')
cur = conn.cursor()
cur.execute("select title from v_person_short;")

list_person = functools.reduce(operator.add,(cur.fetchall()))
print(f'list_person {list_person}')

root = Tk()
root.title("Телефонный справочник")
root.geometry("800x600")

person_var = Variable(value=list_person)
lbox_person = Listbox(listvariable=person_var, height=20, width=30)
lbox_person.pack(anchor=NW, padx=10, pady=10, side=LEFT)

frame1 = ttk.Frame(borderwidth=5, relief=RIDGE, height=200, width=400)

btn_add = Button(text="Добавить контакт")


btn_del = Button(frame1, text="Удалить")
btn_del.pack(padx=10, pady=10, side=TOP)

btn_save = Button(frame1, text="Сохранить")
btn_del.pack(padx=10, pady=10, side=TOP)

frame1.pack(padx=10, pady=10, side=LEFT)
btn_add.pack(anchor=NW, padx=10, pady=10, side=LEFT)
# anchor=NW, 
root.mainloop()

conn.close