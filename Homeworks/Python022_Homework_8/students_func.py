import functools
import operator
import logger


def students_func_create(e_conn, e_cur):
    exec_str = 'SELECT max(student_id)+1 FROM students'
    e_cur.execute(exec_str)
    new_id = functools.reduce(operator.add, (e_cur.fetchone()))
    if new_id == None:
        new_id = 1
    lastname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    cls_numb = int(input('Введите номер класса: '))
    exec_str = f'INSERT INTO students (student_id, lastname, firstname, patronymic, class) VALUES ({new_id}, ' \
               f'"{lastname}", "{firstname}", "{patronymic}", "{cls_numb}")'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Ученик: {lastname} {firstname} {patronymic} из {cls_numb} успешно добавлен')
    logtext = f'В базу был добавлен: [{new_id}] {lastname} {firstname} {patronymic} из {cls_numb} класса'
    logger.exp_txt(logtext)


def students_func_delete(e_conn, e_cur):
    exec_str = 'SELECT max(student_id) FROM students'
    e_cur.execute(exec_str)
    max_number = functools.reduce(operator.add, (e_cur.fetchone()))
    exec_str = 'SELECT min(student_id) FROM students'
    e_cur.execute(exec_str)
    min_number = functools.reduce(operator.add, (e_cur.fetchone()))
    show_student(e_conn, e_cur)
    number = int(input(f'Введите ID человека, которого вы хотели бы удалить {min_number} - {max_number}: '))
    exec_str = f'DELETE from estimates  WHERE student_id = {number}'
    e_cur.execute(exec_str)
    e_conn.commit()
    exec_str = f'DELETE from students  WHERE student_id = {number}'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Ученик с ID: {number} удален из базы')
    show_student(e_conn, e_cur, 'Новый список учеников:')
    logtext = f'Ученик с ID: {number} удален из базы'
    logger.exp_txt(logtext)


def students_func_modify(e_conn, e_cur):
    exec_str = 'SELECT max(student_id) FROM students'
    e_cur.execute(exec_str)
    max_number = functools.reduce(operator.add, (e_cur.fetchone()))
    exec_str = 'SELECT min(student_id) FROM students'
    e_cur.execute(exec_str)
    min_number = functools.reduce(operator.add, (e_cur.fetchone()))
    show_student(e_conn, e_cur)
    number = int(input(f'Введите ID человека, которого вы хотели бы изменить {min_number} - {max_number}: '))
    lastname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    cls_numb = int(input('Введите номер класса: '))
    exec_str = f'UPDATE students set lastname="{lastname}", firstname="{firstname}", ' \
               f'patronymic="{patronymic}", class="{cls_numb}"  WHERE student_id = {number}'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Ученик с ID: {number} успешно изменен')
    show_student(e_conn, e_cur, 'Новый список учеников:')
    logtext = f'Данные ученика с ID: {number} успешно изменены на {lastname} {firstname} {patronymic} класс: {cls_numb}'
    logger.exp_txt(logtext)


def show_student(e_conn, e_cur, text='Список учеников:'):
    exec_str = "select student_id, lastname, firstname, patronymic, class from students;"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список учеников:')
    for index in range(len(buf_list)):
        print(f'ID: {buf_list[index][0]}\t{buf_list[index][1]}\t{buf_list[index][2]}'
              f'\t{buf_list[index][3]}\tКласс: {buf_list[index][4]}')

        logtext = f'ID: {buf_list[index][0]}\t{buf_list[index][1]}\t{buf_list[index][2]}'
        f'\t{buf_list[index][3]}\tКласс: {buf_list[index][4]}'
        logger.exp_txt(logtext)
