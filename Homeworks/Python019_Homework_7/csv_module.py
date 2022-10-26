import csv
import sqlite3


def exp_csv(data, filename):
    with open(f'./export/{filename}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def imp_csv(filename):
    with open(f'./export/{filename}.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = []
        rows_result = []
        for row in reader:
            rows.append(row)

        for i in range(len(rows)):
            for j in range(len(rows[i])):
                if rows[i][j].isdigit():
                    rows[i][j] = int(rows[i][j])
        for elem in rows:
            rows_result.append(tuple(elem))
    return rows_result


def exp_db(e_conn, e_cur):
    # conn = sqlite3.connect(db_path)
    # cur = conn.cursor()

    e_cur.execute("select id_person, lastname, firstname, patronymic, note from persons;")
    list_person = e_cur.fetchall()
 
    e_cur.execute("select id_phone, id_person, id_type, phone_number from phones;")
    list_phones = e_cur.fetchall()
 
    e_cur.execute("select id_type, c_type from types;")
    list_types = e_cur.fetchall()
 
    exp_csv(list_person, 'export_person')
    exp_csv(list_phones, 'export_phones')
    exp_csv(list_types, 'export_types')

    # cur.close()
    # conn.close()


def imp_db(e_conn, e_cur):
    # conn = sqlite3.connect(db_path)
    # cur = conn.cursor()

    imp_test_person = imp_csv('export_person')
    imp_test_phones = imp_csv('export_phones')
    imp_test_types = imp_csv('export_types')
    # print(f'Импорт csv: person {imp_test_person}')
    # print(f'Импорт csv: phones {imp_test_phones}')
    # print(f'Импорт csv: types {imp_test_types}')

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
