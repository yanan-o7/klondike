import random

"""
Вводим игроков в игру (игроки вводят свои псевдонимы)
"""
player_one = input('Write your nickname:\n')
player_two = input('Write your nickname:\n')
player = 1

"""
Создаём поле для игры (заполняем поле 10 на 10 "*", когда игрок будет ставить метку, "*" будет заменяться на "Х")
"""
no_hit = '*'
hit = 'X'
game_board = []
for width in range (10):
    game_board_mini = []
    for hight in range (10):
        game_board_mini.append(no_hit)
    game_board.append(game_board_mini)

"""
Выбираем, кто начнёт
"""
coin_flip = [player_one, player_two]
rng = random.choice(coin_flip)
print(rng, '- you start, you are player 1\n')

print('Playing board:')
print(*game_board, sep='\n')

"""
Определяем ВСЕ варианты проигрыша (для каждой клетки с отметкой проверяем, что нет цепочек из 3 клеток с отметками)
"""
def end(game_board):
    line_3 = 0
    if (game_board[0][0] == hit == game_board[0][1] == game_board[0][2] or game_board[0][0] == hit == game_board[1][0] == game_board[2][0] or game_board[0][0] == hit == game_board[1][1] == game_board[2][2] or
        game_board[1][0] == hit == game_board[1][1] == game_board[1][2] or game_board[1][0] == hit == game_board[2][0] == game_board[3][0] or game_board[1][0] == hit == game_board[2][1] == game_board[3][2] or
        game_board[2][0] == hit == game_board[2][1] == game_board[2][2] or game_board[2][0] == hit == game_board[3][0] == game_board[4][0] or game_board[2][0] == hit == game_board[3][1] == game_board[4][2] or
        game_board[3][0] == hit == game_board[3][1] == game_board[3][2] or game_board[3][0] == hit == game_board[4][0] == game_board[5][0] or game_board[3][0] == hit == game_board[4][1] == game_board[5][2] or
        game_board[4][0] == hit == game_board[4][1] == game_board[4][2] or game_board[4][0] == hit == game_board[5][0] == game_board[6][0] or game_board[4][0] == hit == game_board[5][1] == game_board[6][2] or
        game_board[5][0] == hit == game_board[5][1] == game_board[5][2] or game_board[5][0] == hit == game_board[6][0] == game_board[7][0] or game_board[5][0] == hit == game_board[6][1] == game_board[7][2] or
        game_board[6][0] == hit == game_board[6][1] == game_board[6][2] or game_board[6][0] == hit == game_board[7][0] == game_board[8][0] or game_board[6][0] == hit == game_board[7][1] == game_board[8][2] or
        game_board[7][0] == hit == game_board[7][1] == game_board[7][2] or game_board[7][0] == hit == game_board[8][0] == game_board[9][0] or game_board[7][0] == hit == game_board[7][1] == game_board[8][2] or
        game_board[8][0] == hit == game_board[8][1] == game_board[8][2] or game_board[9][0] == hit == game_board[9][1] == game_board[9][2] or

        game_board[0][1] == hit == game_board[1][1] == game_board[2][1] or game_board[0][1] == hit == game_board[0][2] == game_board[0][3] or game_board[0][1] == hit == game_board[1][2] == game_board[2][3] or
        game_board[1][1] == hit == game_board[2][1] == game_board[3][1] or game_board[1][1] == hit == game_board[1][2] == game_board[3][3] or game_board[1][1] == hit == game_board[2][2] == game_board[3][3] or
        game_board[2][1] == hit == game_board[3][1] == game_board[4][1] or game_board[2][1] == hit == game_board[2][2] == game_board[4][3] or game_board[2][1] == hit == game_board[3][2] == game_board[4][3] or
        game_board[3][1] == hit == game_board[4][1] == game_board[5][1] or game_board[3][1] == hit == game_board[3][2] == game_board[3][3] or game_board[3][1] == hit == game_board[4][2] == game_board[5][3] or
        game_board[4][1] == hit == game_board[5][1] == game_board[6][1] or game_board[4][1] == hit == game_board[4][2] == game_board[6][3] or game_board[4][1] == hit == game_board[5][2] == game_board[6][3] or
        game_board[5][1] == hit == game_board[6][1] == game_board[5][1] or game_board[5][1] == hit == game_board[5][2] == game_board[7][3] or game_board[5][1] == hit == game_board[6][2] == game_board[7][3] or
        game_board[6][1] == hit == game_board[7][1] == game_board[6][1] or game_board[6][1] == hit == game_board[6][2] == game_board[8][3] or game_board[6][1] == hit == game_board[7][2] == game_board[8][3] or
        game_board[7][1] == hit == game_board[8][1] == game_board[7][1] or game_board[7][1] == hit == game_board[7][2] == game_board[9][3] or game_board[7][1] == hit == game_board[8][2] == game_board[9][3] or
        game_board[8][1] == hit == game_board[8][2] == game_board[8][3] or game_board[9][1] == hit == game_board[9][2] == game_board[9][3] or

        game_board[0][2] == hit == game_board[1][2] == game_board[2][2] or game_board[0][2] == hit == game_board[0][3] == game_board[0][4] or game_board[0][2] == hit == game_board[1][3] == game_board[2][4] or
        game_board[1][2] == hit == game_board[2][2] == game_board[3][2] or game_board[1][2] == hit == game_board[1][3] == game_board[3][4] or game_board[1][2] == hit == game_board[2][3] == game_board[3][4] or
        game_board[2][2] == hit == game_board[3][2] == game_board[4][2] or game_board[2][2] == hit == game_board[2][3] == game_board[4][4] or game_board[2][2] == hit == game_board[3][3] == game_board[4][4] or
        game_board[3][2] == hit == game_board[4][2] == game_board[5][2] or game_board[3][2] == hit == game_board[3][3] == game_board[3][4] or game_board[3][2] == hit == game_board[4][3] == game_board[5][4] or
        game_board[4][2] == hit == game_board[5][2] == game_board[6][2] or game_board[4][2] == hit == game_board[4][3] == game_board[6][4] or game_board[4][2] == hit == game_board[5][3] == game_board[6][4] or
        game_board[5][2] == hit == game_board[6][2] == game_board[7][2] or game_board[5][2] == hit == game_board[5][3] == game_board[7][4] or game_board[5][2] == hit == game_board[6][3] == game_board[7][4] or
        game_board[6][2] == hit == game_board[7][2] == game_board[8][2] or game_board[6][2] == hit == game_board[6][3] == game_board[8][4] or game_board[6][2] == hit == game_board[7][3] == game_board[8][4] or
        game_board[7][2] == hit == game_board[8][2] == game_board[9][2] or game_board[7][2] == hit == game_board[7][3] == game_board[9][4] or game_board[7][2] == hit == game_board[8][3] == game_board[9][4] or
        game_board[8][2] == hit == game_board[8][3] == game_board[8][4] or game_board[9][2] == hit == game_board[9][3] == game_board[9][4] or

        game_board[0][3] == hit == game_board[1][3] == game_board[2][3] or game_board[0][3] == hit == game_board[0][4] == game_board[0][5] or game_board[0][3] == hit == game_board[1][4] == game_board[2][5] or
        game_board[1][3] == hit == game_board[2][3] == game_board[3][3] or game_board[1][3] == hit == game_board[1][4] == game_board[3][5] or game_board[1][3] == hit == game_board[2][4] == game_board[3][5] or
        game_board[2][3] == hit == game_board[3][3] == game_board[4][3] or game_board[2][3] == hit == game_board[2][4] == game_board[4][5] or game_board[2][3] == hit == game_board[3][4] == game_board[4][5] or
        game_board[3][3] == hit == game_board[4][3] == game_board[5][3] or game_board[3][3] == hit == game_board[3][4] == game_board[3][5] or game_board[3][3] == hit == game_board[4][4] == game_board[5][5] or
        game_board[4][3] == hit == game_board[5][3] == game_board[6][3] or game_board[4][3] == hit == game_board[4][4] == game_board[6][5] or game_board[4][3] == hit == game_board[5][4] == game_board[6][5] or
        game_board[5][3] == hit == game_board[6][3] == game_board[7][3] or game_board[5][3] == hit == game_board[5][4] == game_board[7][5] or game_board[5][3] == hit == game_board[6][4] == game_board[7][5] or
        game_board[6][3] == hit == game_board[7][3] == game_board[8][3] or game_board[6][3] == hit == game_board[6][4] == game_board[8][5] or game_board[6][3] == hit == game_board[7][4] == game_board[8][5] or
        game_board[7][3] == hit == game_board[8][3] == game_board[9][3] or game_board[7][3] == hit == game_board[7][4] == game_board[9][5] or game_board[7][3] == hit == game_board[8][4] == game_board[9][5] or
        game_board[8][3] == hit == game_board[8][4] == game_board[8][5] or game_board[9][3] == hit == game_board[9][4] == game_board[9][5] or

        game_board[0][4] == hit == game_board[1][4] == game_board[2][4] or game_board[0][4] == hit == game_board[0][5] == game_board[0][6] or game_board[0][4] == hit == game_board[1][5] == game_board[2][6] or
        game_board[1][4] == hit == game_board[2][4] == game_board[3][4] or game_board[1][4] == hit == game_board[1][5] == game_board[3][6] or game_board[1][4] == hit == game_board[2][5] == game_board[3][6] or
        game_board[2][4] == hit == game_board[3][4] == game_board[4][4] or game_board[2][4] == hit == game_board[2][5] == game_board[4][6] or game_board[2][4] == hit == game_board[3][5] == game_board[4][6] or
        game_board[3][4] == hit == game_board[4][4] == game_board[5][4] or game_board[3][4] == hit == game_board[3][5] == game_board[3][6] or game_board[3][4] == hit == game_board[4][5] == game_board[5][6] or
        game_board[4][4] == hit == game_board[5][4] == game_board[6][4] or game_board[4][4] == hit == game_board[4][5] == game_board[6][6] or game_board[4][4] == hit == game_board[5][5] == game_board[6][6] or
        game_board[5][4] == hit == game_board[6][4] == game_board[7][4] or game_board[5][4] == hit == game_board[5][5] == game_board[7][6] or game_board[5][4] == hit == game_board[6][5] == game_board[7][6] or
        game_board[6][4] == hit == game_board[7][4] == game_board[8][4] or game_board[6][4] == hit == game_board[6][5] == game_board[8][6] or game_board[6][4] == hit == game_board[7][5] == game_board[8][6] or
        game_board[7][4] == hit == game_board[8][4] == game_board[9][4] or game_board[7][4] == hit == game_board[7][5] == game_board[9][6] or game_board[7][4] == hit == game_board[8][5] == game_board[9][6] or
        game_board[8][4] == hit == game_board[8][5] == game_board[8][6] or game_board[9][4] == hit == game_board[9][5] == game_board[9][6] or

        game_board[0][5] == hit == game_board[1][5] == game_board[2][5] or game_board[0][5] == hit == game_board[0][6] == game_board[0][7] or game_board[0][5] == hit == game_board[1][6] == game_board[2][7] or
        game_board[1][5] == hit == game_board[2][5] == game_board[3][5] or game_board[1][5] == hit == game_board[1][6] == game_board[3][7] or game_board[1][5] == hit == game_board[2][6] == game_board[3][7] or
        game_board[2][5] == hit == game_board[3][5] == game_board[4][5] or game_board[2][5] == hit == game_board[2][6] == game_board[4][7] or game_board[2][5] == hit == game_board[3][6] == game_board[4][7] or
        game_board[3][5] == hit == game_board[4][5] == game_board[5][5] or game_board[3][5] == hit == game_board[3][6] == game_board[3][7] or game_board[3][5] == hit == game_board[4][6] == game_board[5][7] or
        game_board[4][5] == hit == game_board[5][5] == game_board[6][5] or game_board[4][5] == hit == game_board[4][6] == game_board[6][7] or game_board[4][5] == hit == game_board[5][6] == game_board[6][7] or
        game_board[5][5] == hit == game_board[6][5] == game_board[7][5] or game_board[5][5] == hit == game_board[5][6] == game_board[7][7] or game_board[5][5] == hit == game_board[6][6] == game_board[7][7] or
        game_board[6][5] == hit == game_board[7][5] == game_board[8][5] or game_board[6][5] == hit == game_board[6][6] == game_board[8][7] or game_board[6][5] == hit == game_board[7][6] == game_board[8][7] or
        game_board[7][5] == hit == game_board[8][5] == game_board[9][5] or game_board[7][5] == hit == game_board[7][6] == game_board[9][7] or game_board[7][5] == hit == game_board[8][6] == game_board[9][7] or
        game_board[8][5] == hit == game_board[8][6] == game_board[8][7] or game_board[9][5] == hit == game_board[9][6] == game_board[9][7] or

        game_board[0][6] == hit == game_board[1][6] == game_board[2][6] or game_board[0][6] == hit == game_board[0][7] == game_board[0][8] or game_board[0][6] == hit == game_board[1][7] == game_board[2][8] or
        game_board[1][6] == hit == game_board[2][6] == game_board[3][6] or game_board[1][6] == hit == game_board[1][7] == game_board[3][8] or game_board[1][6] == hit == game_board[2][7] == game_board[3][8] or
        game_board[2][6] == hit == game_board[3][6] == game_board[4][6] or game_board[2][6] == hit == game_board[2][7] == game_board[4][8] or game_board[2][6] == hit == game_board[3][7] == game_board[4][8] or
        game_board[3][6] == hit == game_board[4][6] == game_board[5][6] or game_board[3][6] == hit == game_board[3][7] == game_board[3][8] or game_board[3][6] == hit == game_board[4][7] == game_board[5][8] or
        game_board[4][6] == hit == game_board[5][6] == game_board[6][6] or game_board[4][6] == hit == game_board[4][7] == game_board[6][8] or game_board[4][6] == hit == game_board[5][7] == game_board[6][8] or
        game_board[5][6] == hit == game_board[6][6] == game_board[7][6] or game_board[5][6] == hit == game_board[5][7] == game_board[7][8] or game_board[5][6] == hit == game_board[6][7] == game_board[7][8] or
        game_board[6][6] == hit == game_board[7][6] == game_board[8][6] or game_board[6][6] == hit == game_board[6][7] == game_board[8][8] or game_board[6][6] == hit == game_board[7][7] == game_board[8][8] or
        game_board[7][6] == hit == game_board[8][6] == game_board[9][6] or game_board[7][6] == hit == game_board[7][7] == game_board[9][8] or game_board[7][6] == hit == game_board[8][7] == game_board[9][8] or
        game_board[8][6] == hit == game_board[8][7] == game_board[8][8] or game_board[9][6] == hit == game_board[9][7] == game_board[9][8] or

        game_board[0][7] == hit == game_board[1][7] == game_board[2][7] or game_board[0][7] == hit == game_board[0][8] == game_board[0][3] or game_board[0][7] == hit == game_board[1][8] == game_board[2][9] or
        game_board[1][7] == hit == game_board[2][7] == game_board[3][7] or game_board[1][7] == hit == game_board[1][8] == game_board[3][3] or game_board[1][7] == hit == game_board[2][8] == game_board[3][9] or
        game_board[2][7] == hit == game_board[3][7] == game_board[4][7] or game_board[2][7] == hit == game_board[2][8] == game_board[4][3] or game_board[2][7] == hit == game_board[3][8] == game_board[4][9] or
        game_board[3][7] == hit == game_board[4][7] == game_board[5][7] or game_board[3][7] == hit == game_board[3][8] == game_board[3][3] or game_board[3][7] == hit == game_board[4][8] == game_board[5][9] or
        game_board[4][7] == hit == game_board[5][7] == game_board[6][7] or game_board[4][7] == hit == game_board[4][8] == game_board[6][3] or game_board[4][7] == hit == game_board[5][8] == game_board[6][9] or
        game_board[5][7] == hit == game_board[6][7] == game_board[5][7] or game_board[5][7] == hit == game_board[5][8] == game_board[7][3] or game_board[5][7] == hit == game_board[6][8] == game_board[7][9] or
        game_board[6][7] == hit == game_board[7][7] == game_board[6][7] or game_board[6][7] == hit == game_board[6][8] == game_board[8][3] or game_board[6][7] == hit == game_board[7][8] == game_board[8][9] or
        game_board[7][7] == hit == game_board[8][7] == game_board[7][7] or game_board[7][7] == hit == game_board[7][8] == game_board[9][3] or game_board[7][7] == hit == game_board[8][8] == game_board[9][9] or
        game_board[8][7] == hit == game_board[8][8] == game_board[8][9] or game_board[9][7] == hit == game_board[9][8] == game_board[9][3] or

        game_board[0][8] == hit == game_board[1][8] == game_board[2][8] or
        game_board[1][8] == hit == game_board[2][8] == game_board[3][8] or
        game_board[2][8] == hit == game_board[3][8] == game_board[4][8] or
        game_board[3][8] == hit == game_board[4][8] == game_board[5][8] or
        game_board[4][8] == hit == game_board[5][8] == game_board[6][8] or
        game_board[5][8] == hit == game_board[6][8] == game_board[7][8] or
        game_board[6][8] == hit == game_board[7][8] == game_board[8][8] or
        game_board[7][8] == hit == game_board[8][8] == game_board[9][8] or
        game_board[0][9] == hit == game_board[1][9] == game_board[2][9] or
        game_board[1][9] == hit == game_board[2][9] == game_board[3][9] or
        game_board[2][9] == hit == game_board[3][9] == game_board[4][9] or
        game_board[3][9] == hit == game_board[4][9] == game_board[5][9] or
        game_board[4][9] == hit == game_board[5][9] == game_board[6][9] or
        game_board[5][9] == hit == game_board[6][9] == game_board[7][9] or
        game_board[6][9] == hit == game_board[7][9] == game_board[8][9] or
        game_board[7][9] == hit == game_board[8][9] == game_board[9][9]):
        line_3 = 1
    return line_3

"""
Проверка правильности ввода чисел
"""
def line_check():
    try:
        line = int(input('Chose the line: '))
        return line
    except ValueError:
        print('Write in numbers please')
        return line_check()
def row_check():
    try:
        row = int(input('Now the row: '))
        return row
    except ValueError:
        print('Write in numbers please')
        return row_check()

"""
Ход игры (пока на поле нет цепочек из 3 отметок, игроки по очереди ставят метки, а игрок, создавший цепочку, – проигрывает)
"""
while not end(game_board):
    my_line = line_check()
    my_row = row_check()
    if 0 <= my_row < 10 and 0 <= my_line < 10:
        if game_board[my_line][my_row] != hit:
            game_board[my_line][my_row] = hit
    print('Playing board:')
    print(*game_board, sep='\n')
    player+=1
else:
    print('You Died')
    if player%2 == 0: print('player 1 - you win')
    if player%2 != 0: print('player 2 - you win')
