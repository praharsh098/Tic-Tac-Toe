def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def get_player_move():
    try:
        move = int(input("Enter your move (1-9): ")) - 1
        if 0 <= move < 9:
            return move
        else:
            print("Invalid move. Please choose a number between 1 and 9.")
            return get_player_move()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_player_move()

def make_move(board, player, move):
    row, col = divmod(move, 3)
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("That cell is already taken. Try again.")
        return False

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def play_tic_tac_toe():
    board = initialize_board()
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        move = get_player_move()

        if make_move(board, current_player, move):
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print("The game ends in a tie!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tic_tac_toe()


#have to make a GUI version of this.