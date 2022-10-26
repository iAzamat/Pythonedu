from tkinter import *
from tkinter.ttk import *

def add_item():
    lbox.insert(END, entry.get())
    entry.delete(0, END)

def del_list():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)

def print_list():
    print(lbox.get(0, END))

root = Tk()

lbox = Listbox(selectmode=EXTENDED)
lbox.pack(side=LEFT)
scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)
lbox.config(yscrollcommand=scroll.set)

f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)
entry.pack(anchor=N)
Button(f, text="Add", command=add_item).pack(fill=X)
Button(f, text="Delete", command=del_list).pack(fill=X)
Button(f, text="Print", command=print_list).pack(fill=X)

root.mainloop()