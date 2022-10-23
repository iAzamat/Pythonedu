import functools
import operator
import datetime
import time
import logger


def estimates_func_create(e_conn, e_cur):
    exec_str = 'SELECT max(estimates_id)+1 FROM estimates'
    e_cur.execute(exec_str)
    new_id = functools.reduce(operator.add, (e_cur.fetchone()))
    if new_id == None:
        new_id = 1
    exec_str = 'SELECT subject_id, name FROM subjects'
    e_cur.execute(exec_str)
    list_subjects = e_cur.fetchall()
    for index in range(len(list_subjects)):
        print(f'ID: {list_subjects[index][0]} {list_subjects[index][1]}')
    subject_id = int(input(f'Введите ID предмета по которому ставите оценку: '))

    exec_str = "select student_id, lastname, firstname, patronymic, class from students;"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список учеников:')
    for index in range(len(buf_list)):
        print(f'{buf_list[index][0]}\t{buf_list[index][1]}\t{buf_list[index][2]}'
              f'\t{buf_list[index][3]}\t{buf_list[index][4]}')
    student_id = int(input(f'Введите ID ученика, которому ставите оценку: '))
    estimate = int(input(f'Введите оценку ученика: '))
    date = round(time.time() * 1000)
    exec_str = f'INSERT INTO estimates (estimates_id, subject_id, student_id, time, estimate) VALUES ({new_id}, ' \
               f'"{subject_id}", "{student_id}", "{date}", "{estimate}")'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Оценка успешно выставлена')
    logtext = f'Ученику: {student_id} по предмету: {subject_id} выставлена {estimate}'
    logger.exp_txt(logtext)


def estimates_func_delete(e_conn, e_cur):
    exec_str = "select subject_id, name from subjects;"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список предметов:')
    for index in range(len(buf_list)):
        print(f'{buf_list[index][0]}\t{buf_list[index][1]}')
    subject_id = int(input(f'Введите ID предмета оценку по которому нужно удалить: '))
    exec_str = "select student_id, lastname, firstname, patronymic, class from students;"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список учеников:')
    for index in range(len(buf_list)):
        print(f'{buf_list[index][0]}\t{buf_list[index][1]}\t{buf_list[index][2]}'
              f'\t{buf_list[index][3]}\t{buf_list[index][4]}')

    student_id = int(input(f'Введите ID ученика оценку которого нужно удалить: '))

    exec_str = f"select estimates_id, time, estimate from estimates where (subject_id={subject_id} " \
               f"and student_id={student_id});"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список оценок:')
    for index in range(len(buf_list)):
        date = str(datetime.datetime.fromtimestamp(buf_list[index][1] / 1000.0)).split('.')[0]
        print(f'ID: {buf_list[index][0]}\t{date}\t{buf_list[index][2]}')

    estimates_id = int(input(f'Введите ID оценки которую нужно удалить: '))
    exec_str = f'DELETE from estimates  WHERE estimates_id = {estimates_id}'
    e_cur.execute(exec_str)
    e_conn.commit()

    exec_str = f"select estimates_id, time, estimate from estimates where (subject_id={subject_id} " \
               f"and student_id={student_id});"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Оценка успешна удалена')
    print('Новый список оценок:')
    for index in range(len(buf_list)):
        date = str(datetime.datetime.fromtimestamp(buf_list[index][1] / 1000.0)).split('.')[0]
        print(f'ID: {buf_list[index][0]}\t{date}\t{buf_list[index][2]}')

    logtext = f'Ученику: {student_id} по предмету: {subject_id} удалена оценка {estimates_id}'
    logger.exp_txt(logtext)


def estimates_func_modify(e_conn, e_cur):
    exec_str = "select subject_id, name from subjects;"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список предметов:')
    for index in range(len(buf_list)):
        print(f'{buf_list[index][0]}\t{buf_list[index][1]}')
    subject_id = int(input(f'Введите ID предмета оценку по которому нужно изменить: '))
    exec_str = "select student_id, lastname, firstname, patronymic, class from students;"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список учеников:')
    for index in range(len(buf_list)):
        print(f'{buf_list[index][0]}\t{buf_list[index][1]}\t{buf_list[index][2]}'
              f'\t{buf_list[index][3]}\t{buf_list[index][4]}')

    student_id = int(input(f'Введите ID ученика оценку которого нужно изменить: '))

    exec_str = f"select estimates_id, time, estimate from estimates where (subject_id={subject_id} " \
               f"and student_id={student_id});"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список оценок:')
    for index in range(len(buf_list)):
        date = str(datetime.datetime.fromtimestamp(buf_list[index][1] / 1000.0)).split('.')[0]
        print(f'ID: {buf_list[index][0]}\t{date}\t{buf_list[index][2]}')

    estimates_id = int(input(f'Введите ID оценки которую нужно изменить: '))
    estimate = int(input(f'Введите оценку ученика: '))
    date = round(time.time() * 1000)

    exec_str = f'UPDATE estimates set subject_id="{subject_id}", student_id="{student_id}", ' \
               f'time="{date}", estimate="{estimate}"  WHERE estimates_id = {estimates_id}'
    e_cur.execute(exec_str)
    e_conn.commit()
    print(f'Оценка успешно изменена')
    logtext = f'Ученику: {student_id} по предмету: {subject_id} изменена оценка на {estimate}'
    logger.exp_txt(logtext)


def show_estimates(e_conn, e_cur):
    exec_str = f"select student_id, lastname, firstname, patronymic, class, time, name, estimate from v_full;"
    e_cur.execute(exec_str)
    buf_list = e_cur.fetchall()
    print('Список учеников с оценками:')
    for index in range(len(buf_list)):
        student_id = buf_list[index][0]
        lastname = buf_list[index][1]
        firstname = buf_list[index][2]
        patronymic = buf_list[index][3]
        cls_number = buf_list[index][4]
        date = str(datetime.datetime.fromtimestamp(buf_list[index][5] / 1000.0)).split('.')[0]
        name = buf_list[index][6]
        estimate = buf_list[index][7]
        print('ID: {} ФИО: {} {} {} класс: {} \n\tпредмет: {} оценка: {} дата: {}'.format(
            student_id, lastname, firstname, patronymic, cls_number, name, estimate, date))

        logtext = 'ID: {} ФИО: {} {} {} класс: {} \n\tпредмет: {} оценка: {} дата: {}'.format(
            student_id, lastname, firstname, patronymic, cls_number, name, estimate, date)
        logger.exp_txt(logtext)
