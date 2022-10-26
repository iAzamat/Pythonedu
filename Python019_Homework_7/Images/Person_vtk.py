# import imp
import tkinter as tk
import tkinter.font as tkFont
import sqlite3
import functools
import operator
import phone as p
import json_module
import csv_module
import txt_module


# Обработка события выбора из списка и передача данных в поля ввода
def lst_person_selected(event):
    global pk_sel
    global cur
    global conn
    lst_person.focus()
    sel_str = lst_person.get((lst_person.curselection())[0])
    pk_sel = int(sel_str[0:sel_str.find(".", 0)])
    cur.execute(f"select lastname, firstname, patronymic from persons where id_person = {pk_sel};")
    lastname, firstname, patronymic = cur.fetchone()
    text_ln.set(lastname)
    text_fn.set(firstname)
    text_pn.set(patronymic)


# Удаление контакта
def btn_del_cont_command():
    global pk_sel
    global cur
    global conn

    exec_str = f'DELETE from persons  WHERE id_person = {pk_sel}'
    cur.execute(exec_str)
    conn.commit()
    get_list_person()


# Сохранение изменений контакта
def btn_save_con_command():
    global pk_sel
    global cur
    global conn

    exec_str = f'UPDATE persons set lastname="{ent_lastname.get()}", firstname="{ent_firstname.get()}", patronymic="{ent_patronymic.get()}" WHERE id_person = {pk_sel}'
    cur.execute(exec_str)
    conn.commit()
    get_list_person()
    lst_person.focus()


# Создание нового контакта
def btn_add_cont_command():
    global pk_sel
    global cur
    global conn
    exec_str = 'SELECT max(id_person)+1 FROM Persons'
    cur.execute(exec_str)
    new_id = functools.reduce(operator.add, (cur.fetchone()))
    exec_str = f'INSERT INTO persons (id_person, lastname, firstname, patronymic) VALUES ({new_id}, "{ent_lastname.get()}", "{ent_firstname.get()}", "{ent_patronymic.get()}")'
    cur.execute(exec_str)
    conn.commit()
    get_list_person()


def btn_import_command():
    global conn
    global cur
    json_module.imp_db(conn, cur)
    csv_module.imp_db(conn, cur)
    txt_module.imp_db(conn, cur)
    get_list_person()


def btn_export_command():
    global conn
    global cur
    json_module.exp_db(conn, cur)
    csv_module.exp_db(conn, cur)
    txt_module.exp_db(conn, cur)


def btn_del_phone_command():
    print("command")


def btn_save_phone_command():
    p.add_phone()
    print("command")


# Обновление списка контактов
def get_list_person():
    global cur
    global list_person
    global person_var
    cur.execute("select title from v_person_short;")
    list_person = functools.reduce(operator.add, (cur.fetchall()))
    person_var.set(list_person)


pk_sel = 0
# sel_str = ''
list_person = []

# Установка соединения с БД
conn = sqlite3.connect('./db/phone_book.db')
cur = conn.cursor()
# get_list_person()
# cur.execute("select title from v_person_short;")

# Создание головного окла
root = tk.Tk()

person_var = tk.Variable()
text_fn = tk.StringVar()
text_ln = tk.StringVar()
text_pn = tk.StringVar()
get_list_person()

# setting title
root.title("Телефонный справочник")
# setting window size
width = 622
height = 504
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

lbl_title = tk.Label(root)
ft = tkFont.Font(family='Serif', size=10)
lbl_title["font"] = ft
lbl_title["fg"] = "#333333"
lbl_title["justify"] = "center"
lbl_title["text"] = "Контакты"
lbl_title["relief"] = "flat"
lbl_title.place(x=100, y=10, width=70, height=25)

# Листбокс контактов
lst_person = tk.Listbox(root)
lst_person["borderwidth"] = "3px"
ft = tkFont.Font(family='Serif', size=10)
lst_person["font"] = ft
lst_person["fg"] = "#333333"
lst_person["justify"] = "left"
person_var = tk.Variable(value=list_person)
lst_person["listvariable"] = person_var
lst_person["selectmode"] = tk.SINGLE
lst_person.bind("<<ListboxSelect>>", lst_person_selected)  # Привязка события Select
lst_person.place(x=30, y=40, width=219, height=386)

# Кнопки контактов
btn_add_cont = tk.Button(root)
btn_add_cont["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Serif', size=10)
btn_add_cont["font"] = ft
btn_add_cont["fg"] = "#000000"
btn_add_cont["justify"] = "center"
btn_add_cont["text"] = "Добавить контакт"
btn_add_cont.place(x=30, y=440, width=120, height=25)
btn_add_cont["command"] = btn_add_cont_command

btn_save_cont = tk.Button(root)
btn_save_cont["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Serif', size=10)
btn_save_cont["font"] = ft
btn_save_cont["fg"] = "#000000"
btn_save_cont["justify"] = "center"
btn_save_cont["text"] = "Сохранить контакт"
btn_save_cont.place(x=160, y=440, width=120, height=25)
btn_save_cont["command"] = btn_save_con_command

btn_del_cont = tk.Button(root)
btn_del_cont["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Serif', size=10)
btn_del_cont["font"] = ft
btn_del_cont["fg"] = "#000000"
btn_del_cont["justify"] = "center"
btn_del_cont["text"] = "Удалить контакт"
btn_del_cont.place(x=290, y=440, width=120, height=25)
btn_del_cont["command"] = btn_del_cont_command

# Кнопка импорта
btn_import = tk.Button(root)
btn_import["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Serif', size=10)
btn_import["font"] = ft
btn_import["fg"] = "#000000"
btn_import["justify"] = "center"
btn_import["text"] = "Импорт контактов"
btn_import.place(x=480, y=440, width=120, height=25)
btn_import["command"] = btn_import_command

# Кнопка экспорта
btn_export = tk.Button(root)
btn_export["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Serif', size=10)
btn_export["font"] = ft
btn_export["fg"] = "#000000"
btn_export["justify"] = "center"
btn_export["text"] = "Экспорт контактов"
btn_export.place(x=480, y=400, width=120, height=25)
btn_export["command"] = btn_export_command

lbl_lastname = tk.Label(root)
ft = tkFont.Font(family='Serif', size=10)
lbl_lastname["font"] = ft
lbl_lastname["fg"] = "#333333"
lbl_lastname["justify"] = "right"
lbl_lastname["text"] = "Фамилия"
lbl_lastname.place(x=260, y=80, width=70, height=25)

# Поля ввода
ent_lastname = tk.Entry(root)
ent_lastname["borderwidth"] = "2px"
ft = tkFont.Font(family='Serif', size=10)
ent_lastname["font"] = ft
ent_lastname["fg"] = "#333333"
ent_lastname["justify"] = "left"
ent_lastname["text"] = "Entry"
ent_lastname["textvariable"] = text_ln
# lst_person.bind("<<ListboxSelect>>", lst_person_selected)
ent_lastname.place(x=340, y=80, width=250, height=30)

lbl_firstname = tk.Label(root)
ft = tkFont.Font(family='Serif', size=10)
lbl_firstname["font"] = ft
lbl_firstname["fg"] = "#333333"
lbl_firstname["justify"] = "right"
lbl_firstname["text"] = "Имя"
ent_lastname["textvariable"] = text_ln
lbl_firstname.place(x=260, y=130, width=70, height=25)

ent_firstname = tk.Entry(root)
ent_firstname["borderwidth"] = "2px"
ft = tkFont.Font(family='Serif', size=10)
ent_firstname["font"] = ft
ent_firstname["fg"] = "#333333"
ent_firstname["justify"] = "left"
ent_firstname["text"] = "Entry"
ent_firstname["textvariable"] = text_fn
ent_firstname.place(x=340, y=130, width=245, height=30)

lbl_patronymic = tk.Label(root)
ft = tkFont.Font(family='Serif', size=10)
lbl_patronymic["font"] = ft
lbl_patronymic["fg"] = "#333333"
lbl_patronymic["justify"] = "right"
lbl_patronymic["text"] = "Отчество"
lbl_patronymic.place(x=260, y=180, width=70, height=25)

ent_patronymic = tk.Entry(root)
ent_patronymic["borderwidth"] = "2px"
ft = tkFont.Font(family='Serif', size=10)
ent_patronymic["font"] = ft
ent_patronymic["fg"] = "#333333"
ent_patronymic["justify"] = "left"
ent_patronymic["text"] = "Entry"
ent_patronymic["textvariable"] = text_pn
ent_patronymic.place(x=340, y=180, width=247, height=30)

lbl_phone_num = tk.Label(root)
ft = tkFont.Font(family='Serif', size=10)
lbl_phone_num["font"] = ft
lbl_phone_num["fg"] = "#333333"
lbl_phone_num["justify"] = "right"
lbl_phone_num["text"] = "Телефоны"
lbl_phone_num.place(x=260, y=230, width=70, height=25)

# Список телефонов
lst_phone_num = tk.Listbox(root)
lst_phone_num["borderwidth"] = "2px"
ft = tkFont.Font(family='Serif', size=10)
lst_phone_num["font"] = ft
lst_phone_num["fg"] = "#333333"
lst_phone_num["justify"] = "center"
lst_phone_num.place(x=340, y=230, width=247, height=91)

# Кнопки телефонов

btn_save_phone = tk.Button(root)
btn_save_phone["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Serif', size=10)
btn_save_phone["font"] = ft
btn_save_phone["fg"] = "#000000"
btn_save_phone["justify"] = "center"
btn_save_phone["text"] = "Сохранить"
btn_save_phone.place(x=490, y=340, width=70, height=25)
btn_save_phone["command"] = btn_save_phone_command

btn_del_phone = tk.Button(root)
btn_del_phone["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Serif', size=10)
btn_del_phone["font"] = ft
btn_del_phone["fg"] = "#000000"
btn_del_phone["justify"] = "center"
btn_del_phone["text"] = "Удалить"
btn_del_phone.place(x=360, y=340, width=70, height=25)
btn_del_phone["command"] = btn_del_phone_command

# GMessage_847=tk.Message(root)
# ft = tkFont.Font(family='Serif',size=10)
# GMessage_847["font"] = ft
# GMessage_847["fg"] = "#333333"
# GMessage_847["justify"] = "center"
# GMessage_847["text"] = "Ошибка!"
# GMessage_847.place(x=200,y=470,width=80,height=25)

root.mainloop()
