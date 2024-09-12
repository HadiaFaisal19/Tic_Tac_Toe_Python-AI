import random

rows = 3
cols = 3
USER = "0"
AGENT = "X"

def print_board(board):
    for row in board:
        print(row)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def board_full(board):
    return all(cell != '_' for row in board for cell in row)

def user_input(board):
    while True:
        user_row = int(input("Enter the row where you want to place (0, 1, or 2): "))
        user_col = int(input("Enter the column where you want to place (0, 1, or 2): "))

        if 0 <= user_row < rows and 0 <= user_col < cols and board[user_row][user_col] == '_':
            return user_row, user_col
        else:
            print("Invalid input. Please choose an empty space.")

def agent_input(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                board[row][col] = AGENT
                if check_winner(board, AGENT):
                    board[row][col] = '_'
                    return row, col
                board[row][col] = '_'

    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                board[row][col] = USER
                if check_winner(board, USER):
                    board[row][col] = AGENT
                    return row, col
                board[row][col] = '_'

    while True:
        agent_row = random.randint(0, rows - 1)
        agent_col = random.randint(0, cols - 1)

        if board[agent_row][agent_col] == '_':
            return agent_row, agent_col

def play_game():
    two_d_array = [['_' for j in range(cols)] for i in range(rows)]

    while True:
        user_row, user_col = user_input(two_d_array)
        two_d_array[user_row][user_col] = USER
        print("Your move:")
        print_board(two_d_array)

        if check_winner(two_d_array, USER):
            print("You won!")
            break

        if board_full(two_d_array):
            print("It's a tie!")
            break

        agent_row, agent_col = agent_input(two_d_array)
        two_d_array[agent_row][agent_col] = AGENT
        print("Agent's move:")
        print_board(two_d_array)

        if check_winner(two_d_array, AGENT):
            print("Agent won!")
            break

        if board_full(two_d_array):
            print("It's a tie!")
            break

play_game()