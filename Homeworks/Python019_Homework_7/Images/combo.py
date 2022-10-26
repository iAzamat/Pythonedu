from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
languages = ["Python", "C#", "Java", "JavaScript"]
# по умолчанию будет выбран первый элемент из languages
languages_var = StringVar(value=languages[0])   
 
label = ttk.Label(textvariable=languages_var)
label.pack(anchor=NW, padx=6, pady=6)
 
combobox = ttk.Combobox(textvariable=languages_var, values=languages)
combobox.pack(anchor=NW, padx=6, pady=6)
 
print(combobox.get())
root.mainloop()