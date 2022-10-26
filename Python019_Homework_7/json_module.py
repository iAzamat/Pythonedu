import json
import sqlite3


def imp_json(filename):
    with open(f'./export/{filename}.json', 'r', encoding='utf-8') as f:
        buf_list = json.load(f)
        res_list = []
        for elem in buf_list:
            res_list.append(tuple(elem))
        return res_list


def exp_json(data, filename):
    with open(f'./export/{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


def exp_db(e_conn, e_cur):
    # conn = sqlite3.connect(db_path)
    # cur = conn.cursor()

    e_cur.execute("select id_person, lastname, firstname, patronymic, note from persons;")
    list_person = e_cur.fetchall()
    # print(f'list_person {list_person}')

    e_cur.execute("select id_phone, id_person, id_type, phone_number from phones;")
    list_phones = e_cur.fetchall()
    # print(f'list_phones {list_phones}')

    e_cur.execute("select id_type, c_type from types;")
    list_types = e_cur.fetchall()
    # print(f'list_types {list_types}')

    exp_json(list_person, 'export_person')
    exp_json(list_phones, 'export_phones')
    exp_json(list_types, 'export_types')

    # cur.close()
    # conn.close()


def imp_db(e_conn, e_cur):
    # conn = sqlite3.connect(db_path)
    # cur = conn.cursor()

    imp_test_person = imp_json('export_person')
    imp_test_phones = imp_json('export_phones')
    imp_test_types = imp_json('export_types')
    # print(f'Импорт json: person {imp_test_person}')
    # print(f'Импорт json: phones {imp_test_phones}')
    # print(f'Импорт json: types {imp_test_types}')

    for i in range(len(imp_test_person)):
        exec_str = f'REPLACE INTO persons (id_person, lastname, firstname, patronymic, note) VALUES ' \
                   f'({imp_test_person[i][0]}, "{imp_test_person[i][1]}", "{imp_test_person[i][2]}", ' \
                   f'"{imp_test_person[i][3]}", "{imp_test_person[i][4]}")'
        e_cur.execute(exec_str)
        e_conn.commit()

    for j in range(len(imp_test_phones)):
        exec_str = f'REPLACE INTO phones (id_phone, id_person, id_type, phone_number) VALUES ' \
                   f'({imp_test_phones[j][0]}, "{imp_test_phones[j][1]}", "{imp_test_phones[j][2]}", ' \
                   f'"{imp_test_phones[j][3]}")'
        e_cur.execute(exec_str)
        e_conn.commit()

    for k in range(len(imp_test_types)):
        exec_str = f'REPLACE INTO types (id_type, c_type) VALUES ' \
                   f'({imp_test_types[k][0]}, "{imp_test_types[k][1]}")'
        e_cur.execute(exec_str)
        e_conn.commit()

    # cur.close()
    # conn.close()
