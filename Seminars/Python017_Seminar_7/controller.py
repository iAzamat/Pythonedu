
import complex_calc as cc
import real_calc as rc
import view
import logger as log


def button_click():
    value_a = view.get_value()
    value_op = view.get_op()
    value_b = view.get_value()

    if 'i' in value_a or 'i' in value_b:
        value_a_lst = list(map(int, value_a.replace('i', '').split('+')))
        value_b_lst = list(map(int, value_b.replace('i', '').split('+')))
        cc.init(value_a_lst, value_b_lst)
        result = cc.do_it(value_op)
        log_res = view.view_data_lst(result, "result")
        log_str = f'{value_a} {value_op} {value_b} = {log_res}'
    else:
        value_a = int(value_a)
        value_b = int(value_b)
        rc.init(value_a, value_b)
        result = rc.do_it(value_op)
        view.view_data(result, "result")
        log_str = f'{value_a} {value_op} {value_b} = {result}'

    log.log_operation(log_str)


if __name__ == '__main__':
    button_click()

