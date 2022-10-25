from new_person import writing_down as wd
import view
import json_module as jm
t_book = wd()
view.export_book(t_book)
jm.exp_json(t_book, filename = 'TelephoneBook')