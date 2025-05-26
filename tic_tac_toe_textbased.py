def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)


def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column: 1 1): ")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1
            if board[row][col] not in ['X', 'O']:
                return row, col
            else:
                print("Cell already taken. Choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Enter two numbers between 1 and 3 separated by space.")


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tic-Tac-Toe (2 Players)!")
    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()
