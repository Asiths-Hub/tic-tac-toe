def print_board(board_list):
    for row in board_list:
        print(f"{row[0]} | {row[1]} | {row[2]}")
        print("-"*10)


def check_win(board_list, player):
    # check for rows
    for row in board_list:
        if all(val == player for val in row):
            return True
    # check for columns
    for col in range(3):
        if all(row[col] == player for row in board_list):
            return True
    # check for diagonals
    if all(board_list[i][i] == player for i in range(3)):
        return True
    if all(board_list[i][2-i] == player for i in range(3)):
        return True


def check_draw(board_list):
    if all(cell != ' ' for row in board_list for cell in row):
        return True


def tic_tac_toe():
    # make an empty list to store values using list comprehension
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_on = True
    while game_on:
        # using try catch method to catch the error of enter without values
        try:
            rw = int(input("Please enter row value(0,1,2)? "))
            col = int(input("Please enter column value(0,1,2)? "))
            # validate inputs
            if rw not in range(3) or col not in range(3):
                print("The row/column value should be in (0,1,2) range. check and re enter again.")
                continue
            if board[rw][col] != ' ':
                print("Cell is already taken")
                continue
            board[rw][col] = current_player
        except ValueError:
            print("Enter a valid Input")
            continue
        if check_draw(board):
            print("It is a draw!")
            break
        print_board(board)
        if check_win(board, current_player):
            print(f"{current_player} won the game!")
            break
        current_player = 'O' if current_player == 'X' else 'X'


tic_tac_toe()
