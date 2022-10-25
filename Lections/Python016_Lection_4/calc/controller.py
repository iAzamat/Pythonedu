import model_sum as model
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result, "result")


# if __name__ == '__main__':
#     button_click()

# button_click()



