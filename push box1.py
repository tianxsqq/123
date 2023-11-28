def print_board(board):
    for row in board:
        print(" ".join(row))

def move_player(board, direction):
    player_row, player_col = find_player(board)

    if direction == "up":
        if board[player_row - 1][player_col] != "#":
            if board[player_row - 1][player_col] == "$":
                if board[player_row - 2][player_col] != "#" and board[player_row - 2][player_col] != "$":
                    board[player_row - 2][player_col] = "$"
                    board[player_row - 1][player_col] = "@"
                    board[player_row][player_col] = " "
            else:
                board[player_row - 1][player_col] = "@"
                board[player_row][player_col] = " "
    elif direction == "down":
        if board[player_row + 1][player_col] != "#":
            if board[player_row + 1][player_col] == "$":
                if board[player_row + 2][player_col] != "#" and board[player_row + 2][player_col] != "$":
                    board[player_row + 2][player_col] = "$"
                    board[player_row + 1][player_col] = "@"
                    board[player_row][player_col] = " "
            else:
                board[player_row + 1][player_col] = "@"
                board[player_row][player_col] = " "
    elif direction == "left":
        if board[player_row][player_col - 1] != "#":
            if board[player_row][player_col - 1] == "$":
                if board[player_row][player_col - 2] != "#" and board[player_row][player_col - 2] != "$":
                    board[player_row][player_col - 2] = "$"
                    board[player_row][player_col - 1] = "@"
                    board[player_row][player_col] = " "
            else:
                board[player_row][player_col - 1] = "@"
                board[player_row][player_col] = " "
    elif direction == "right":
        if board[player_row][player_col + 1] != "#":
            if board[player_row][player_col + 1] == "$":
                if board[player_row][player_col + 2] != "#" and board[player_row][player_col + 2] != "$":
                    board[player_row][player_col + 2] = "$"
                    board[player_row][player_col + 1] = "@"
                    board[player_row][player_col] = " "
            else:
                board[player_row][player_col + 1] = "@"
                board[player_row][player_col] = " "

def find_player(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "@":
                return i, j

board = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "$", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
]

while True:
    print_board(board)
    print("Enter 'w' for up, 's' for down, 'a' for left, 'd' for right, or 'q' to quit.")
    direction = input("Your move: ")

    if direction == "q":
        break

    move_player(board, direction)

    if all("$" not in row for row in board):
        print("Congratulations! You won!")
        break
