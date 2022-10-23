import students_func as stf
import subjects_func as suf
import estimates_func as esf
import logger



def changecmd(conn, cur):
    num = -1
    while num != 0:
        print('')
        print('Добавить - (11)\изменить - (12)\удалить - (13) ученика в базе данных')
        print('Выставить - (21)\изменить - (22)\удалить - (23) оценку ученику')
        print('Добавить - (31)\изменить - (32)\удалить - (33) предмет в базе данных')
        print('Показать список: учеников - (41)\предметов - (42)\учеников с оценками - (43)')
        num = int(input('Выберете команду (0 - выход): '))
        if num == 11:
            logger.exp_txt(f'Была выбрана команда: {num}')
            stf.students_func_create(conn, cur)
        elif num == 12:
            logger.exp_txt(f'Была выбрана команда: {num}')
            stf.students_func_modify(conn, cur)
        elif num == 13:
            logger.exp_txt(f'Была выбрана команда: {num}')
            stf.students_func_delete(conn, cur)
        elif num == 21:
            logger.exp_txt(f'Была выбрана команда: {num}')
            esf.estimates_func_create(conn, cur)
        elif num == 22:
            logger.exp_txt(f'Была выбрана команда: {num}')
            esf.estimates_func_modify(conn, cur)
        elif num == 23:
            logger.exp_txt(f'Была выбрана команда: {num}')
            esf.estimates_func_delete(conn, cur)
        elif num == 31:
            logger.exp_txt(f'Была выбрана команда: {num}')
            suf.subjects_func_create(conn, cur)
        elif num == 32:
            logger.exp_txt(f'Была выбрана команда: {num}')
            suf.subjects_func_modify(conn, cur)
        elif num == 33:
            logger.exp_txt(f'Была выбрана команда: {num}')
            suf.subjects_func_delete(conn, cur)
        elif num == 41:
            logger.exp_txt(f'Была выбрана команда: {num}')
            stf.show_student(conn, cur)
        elif num == 42:
            logger.exp_txt(f'Была выбрана команда: {num}')
            suf.show_subjects(conn, cur)
        elif num == 43:
            logger.exp_txt(f'Была выбрана команда: {num}')
            esf.show_estimates(conn, cur)
        else:
            if num:
                print('такой команды нет')

        logger.exp_txt(f'Была выбрана команда: {num}')
