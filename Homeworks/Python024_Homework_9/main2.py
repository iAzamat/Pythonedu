from tkinter import *
import random

root = Tk()
root.title('Крестики-нолики')
game_run = True
field = []
cross_count = 0


def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = '#F5F5DC'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0
    desc["text"] = ""


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = chr(10060)
        global cross_count
        cross_count += 1
        check_win(chr(10060))
        if cross_count == 5:
            desc["text"] = "Ничья"
        if game_run and cross_count < 5:
            computer_move()
            check_win(chr(11093))


def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)


def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = '#F08080'
        global game_run
        game_run = False
        desc["text"] = f"Победа {smb}"


def can_win(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = chr(11093)
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = chr(11093)
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = chr(11093)
        res = True
    return res


def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], chr(11093)):
            return
        if can_win(field[0][n], field[1][n], field[2][n], chr(11093)):
            return
    if can_win(field[0][0], field[1][1], field[2][2], chr(11093)):
        return
    if can_win(field[2][0], field[1][1], field[0][2], chr(11093)):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], chr(10060)):
            return
        if can_win(field[0][n], field[1][n], field[2][n], chr(10060)):
            return
    if can_win(field[0][0], field[1][1], field[2][2], chr(10060)):
        return
    if can_win(field[2][0], field[1][1], field[0][2], chr(10060)):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = chr(11093)
            break


for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='#F5F5DC',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
desc = Label(text="")
desc.grid(row=3, column=1)
new_button = Button(root, text='Новая игра', command=new_game)
new_button.grid(row=4, column=0, columnspan=3, sticky='nsew')
root.mainloop()
