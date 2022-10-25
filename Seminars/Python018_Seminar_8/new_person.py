import telephone_book as tb
import view


def writing_down():
    name = view.get_name()
    phone = view.get_number()
    action = view. what_to_do()
    if action == 'новый контакт':
        if name[0] not in tb.t_book:
            tb.create_new_list(name, tb.t_book)
        tb.create_new_note(name, tb.t_book, phone)
    elif action == 'смена номера':
        tb.update_note(name, tb.t_book, phone)
    elif action == 'дополнительный номер':
        tb.append_number(name, phone, tb.t_book)
    elif action == 'удалить номер':
        tb.delete_note(name, tb.t_book)
    return tb.t_book
    






