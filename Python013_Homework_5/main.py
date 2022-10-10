import random

'''
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''


def task1():
    text = 'съешь ещёабв этих мягабвких французских булок, да выпей чаю абв'
    my_list = list(filter(lambda x: 'абв' not in x, text.split()))
    print(' '.join(my_list))


'''
2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''


def protectinput(maxcand=28):
    num = input(f'Введите число конфет: ')
    while not num.isdigit():
        num = input(f'Введите число конфет: ')
    if 0 < int(num) < maxcand + 1:
        return num
    else:
        return protectinput()


def playervsplayer():
    numberofcandies = 2021
    max_candie = 28
    players = {1: 'Player1', 2: 'Player2'}
    players[1] = input('Введите имя первого игрока: ')
    players[2] = input('Введите имя второго игрока: ')
    move_start = random.randint(1, 2)
    print(f'По результатам жеребьевки первым ходит: <<{players[move_start]}>>')
    number = int(protectinput())
    numberofcandies = numberofcandies - number
    print(f'<<{players[move_start]}>> забрал {number} конфет. Осталось: {numberofcandies} конфеты')
    move = 1 if move_start == 2 else 2

    while numberofcandies > max_candie:
        print(f'Ходит <<{players[move]}>>')
        number = int(protectinput())
        numberofcandies = numberofcandies - number
        print(f'<<{players[move]}>> забрал {number} конфет. Осталось: {numberofcandies} конфеты')
        move = 1 if move == 2 else 2

    else:
        print(f'Победил: <<{players[move]}>>')


def playervseasybot():
    numberofcandies = 2021
    max_candie = 28
    players = {1: 'Player1', 2: 'Easy Bot'}
    players[1] = input('Введите имя игрока: ')

    move_start = random.randint(1, 2)
    print(f'По результатам жеребьевки первым ходит: <<{players[move_start]}>>')
    if players[move_start] == players[2]:
        number = random.randint(1, max_candie)
    else:
        number = int(protectinput())
    numberofcandies = numberofcandies - number
    print(f'<<{players[move_start]}>> забрал {number} конфет. Осталось: {numberofcandies} конфеты')
    move = 1 if move_start == 2 else 2

    while numberofcandies > max_candie:
        print(f'Ходит <<{players[move]}>>')
        if players[move] == players[2]:
            number = random.randint(1, max_candie)
        else:
            number = int(protectinput())
        numberofcandies = numberofcandies - number
        print(f'<<{players[move]}>> забрал {number} конфет. Осталось: {numberofcandies} конфеты')
        move = 1 if move == 2 else 2

    else:
        print(f'Победил: <<{players[move]}>>')


def playervshardbot():
    numberofcandies = 2021
    max_candie = 28
    players = {1: 'Player1', 2: 'Hard Bot'}
    players[1] = input('Введите имя игрока: ')

    move_start = random.randint(1, 2)
    print(f'По результатам жеребьевки первым ходит: <<{players[move_start]}>>')
    bot_first = False
    if players[move_start] == players[2]:
        number = numberofcandies % (max_candie + 1)
        bot_first = True
    else:
        number = int(protectinput())
    numberofcandies = numberofcandies - number
    print(f'<<{players[move_start]}>> забрал {number} конфет. Осталось: {numberofcandies} конфеты')
    move = 1 if move_start == 2 else 2

    while numberofcandies > max_candie:
        print(f'Ходит <<{players[move]}>>')
        if players[move] == players[2]:
            if (bot_first == False) and (numberofcandies % (max_candie + 1)) != 0:
                number = numberofcandies % (max_candie + 1)
                bot_first = True
                # print('1 выполнено')
            elif (bot_first == False) and (numberofcandies % (max_candie + 1)) == 0:
                number = random.randint(1, max_candie)
                # print('2 выполнено')
            else:
                number = (max_candie + 1) - number
                # print('3 выполнено')
        else:
            number = int(protectinput())
        numberofcandies = numberofcandies - number
        print(f'<<{players[move]}>> забрал {number} конфет. Осталось: {numberofcandies} конфеты')
        move = 1 if move == 2 else 2
    else:
        print(f'Победил: <<{players[move]}>>')


def task2():
    # playervsplayer()
    # playervseasybot()
    playervshardbot()


'''
3. Создайте программу для игры в ""Крестики-нолики"".
'''


def draw_board(board):
    print('-' * 25)
    for i in range(3):
        print(f'|\t{board[0 + i * 3]}\t|\t{board[1 + i * 3]}\t|\t{board[2 + i * 3]}\t|')
        print('-' * 25)


def take_input(player_token, board):
    valid = False
    while not valid:
        player_answer = input(f'Куда поставим {player_token}? Введите число 1 - 9: ')
        try:
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод. Вы уверены, что ввели число?')
            continue
        if 1 <= player_answer <= 9:
            if (str(board[player_answer - 1]) not in 'XO'):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('Эта клетка уже занята!')
        else:
            print('Некорректный ввод. Введите число от 1 до 9')


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X', board)
        else:
            take_input('0', board)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    draw_board(board)


def task3():
    print(f'{"*" * 10} Игра крестики-нолики для двух игроков {"*" * 10}')
    board = [i for i in range(1, 10)]
    main(board)


'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
Пример:
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные: 12W1B12W3B24W1B14W
'''


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


def rle_encodefile(filename='file1'):
    with open(f'{filename}.txt', 'r') as f:
        inp_value = f.read()
        encoded_val = rle_encode(inp_value)

    with open(f'{filename}_encode.txt', 'w') as f:
        f.write(encoded_val)

    print(f'Исходные данные: {inp_value}\nЗакодированные данные: {encoded_val}')


def rle_decodefile(filename='file2'):
    with open(f'{filename}.txt', 'r') as f:
        inp_value = f.read()
        decoded_val = rle_decode(inp_value)

    with open(f'{filename}_decode.txt', 'w') as f:
        f.write(decoded_val)

    print(f'Исходные данные: {inp_value}\nДекодированные данные: {decoded_val}')


def task4():
    rle_encodefile('file1')
    rle_decodefile('file2')


# task1()
# task2()
# task3()
# task4()
