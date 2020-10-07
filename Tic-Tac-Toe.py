"""Tic-Tac-Toe"""
import random


def play_game():
    possible_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    position_of_player = []  # player is O
    position_of_opponent = []  # computer is X
    selected_position = []
    unselected_pos = list(set(possible_positions) - set(selected_position))
    # row1[1] = pos1, row1[5] = pos2, row1[9] = pos3
    # row3[1] = pos4, row3[5] = pos5, row3[9] = pos6
    # row5[1] = pos7, row5[5] = pos8, row5[9] = pos9
    row1 = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
    row2 = ["-", "-", "-", "|", "-", "-", "-", "|", "-", "-", "-"]
    row3 = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
    row4 = ["-", "-", "-", "|", "-", "-", "-", "|", "-", "-", "-"]
    row5 = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]
    victory_condition = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    almost_win = []
    for i in range(len(victory_condition)):
        for j in range(len(victory_condition[i])):
            sub_list = []
            for k in range(len(victory_condition[i])):
                if k == j:
                    continue
                sub_list.append(victory_condition[i][k])
            sub_list.append(victory_condition[i][j])
            almost_win.append(sub_list)
    # print(almost_win)

    print("Player is O and Computer is X")

    while check_victory(victory_condition, position_of_player) is False and check_victory(victory_condition, position_of_opponent) is False:
        print_33_grid(row1, row2, row3, row4, row5)
        # print(unselected_pos)
        # print(selected_position)
        try:
            new_pos = int(input("Please make your move! [1-9]: "))
        except:
            print("Invalid input! Please input an integer from 1 to 9")
            continue
        if new_pos > 9 or new_pos < 1 or new_pos in position_of_player or new_pos in position_of_opponent:
            print("Invalid input!")
            continue
        selected_position.append(new_pos)
        position_of_player.append(new_pos)
        unselected_pos = list(set(possible_positions) - set(selected_position))
        position_update(new_pos, row1, row3, row5, "O")

        # if player wins
        if check_victory(victory_condition, position_of_player) is True:
            print_33_grid(row1, row2, row3, row4, row5)
            print("Congratulations! You won!")
            break
        # if neither wins
        if len(unselected_pos) == 0:
            print_33_grid(row1, row2, row3, row4, row5)
            print("It's a draw!")
            break
        ai_new_pos = ai(position_of_player, position_of_opponent, almost_win, unselected_pos)
        selected_position.append(ai_new_pos)
        position_of_opponent.append(ai_new_pos)
        unselected_pos = list(set(possible_positions) - set(selected_position))
        position_update(ai_new_pos, row1, row3, row5, "X")
        # if computer wins
        if check_victory(victory_condition, position_of_opponent) is True:
            print_33_grid(row1, row2, row3, row4, row5)
            print("You lost!")
            break
        # if neither wins (just in case)
        if len(unselected_pos) == 0:
            print_33_grid(row1, row2, row3, row4, row5)
            print("It's a draw!")
            break


def print_33_grid(a, b, c, d, e):
    print("".join(a))
    print("".join(b))
    print("".join(c))
    print("".join(d))
    print("".join(e))


def check_victory(condition, position):
    for i in range(len(condition)):
        if set(condition[i]) <= set(position):
            return True
    return False


def position_update(pos: int, a: list, c: list, e: list, symbol: str):
    if pos % 3 == 1:
        index = 1
    elif pos % 3 == 2:
        index = 5
    else:
        index = 9
    if pos <= 3:
        a[index] = symbol
    elif pos <= 6:
        c[index] = symbol
    else:
        e[index] = symbol


def ai(player: list, opponent: list, condition: list, unselected: list):  # returns new position of computer
    for i in range(len(condition)):
        if set(condition[i][:2]) <= set(opponent):
            if not condition[i][2] in opponent and not condition[i][2] in player:
                return condition[i][2]
    for i in range(len(condition)):
        if set(condition[i][:2]) <= set(player):
            if not condition[i][2] in opponent and not condition[i][2] in player:
                return condition[i][2]
    for i in range(len(condition)):
        for j in range(len(opponent)):
            if opponent[j] == condition[i][2]:
                if set(condition[i][:2]) <= set(unselected):
                    random.choice(condition[i][:2])
    return random.choice(unselected)


if __name__ == '__main__':
    play_game()
