import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def evaluate(board):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    else:
        return 0

def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth+1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth+1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def ai_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = "X"

def play_game():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not check_winner(board, "X") and not check_winner(board, "O") and not is_board_full(board):
        player_move = input("Enter your move (row[1-3] column[1-3]): ")
        row, col = map(int, player_move.split())
        if board[row-1][col-1] == " ":
            board[row-1][col-1] = "O"
            print_board(board)
            if check_winner(board, "O"):
                print("Congratulations! You win!")
                break
            elif is_board_full(board):
                print("It's a draw!")
                break
            ai_move(board)
            print("AI's move:")
            print_board(board)
            if check_winner(board, "X"):
                print("AI wins!")
                break
            elif is_board_full(board):
                print("It's a draw!")
                break
        else:
            print("That cell is already occupied!")

if __name__ == "__main__":
    play_game()
