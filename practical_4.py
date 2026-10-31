# Develop a Tic-Tac-Toe AI using Minimax Algorithm with Alpha-Beta
# Pruning

import math

# Display the Tic-Tac-Toe board
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

# Check winner
def check_winner(board):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None

# Check if game is over
def is_game_over(board):
    return check_winner(board) is not None or " " not in board

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):

    winner = check_winner(board)

    if winner == "X":
        return 10 - depth

    if winner == "O":
        return depth - 10

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(
                    board, depth + 1, alpha, beta, False
                )

                board[i] = " "

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                if beta <= alpha:
                    break

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(
                    board, depth + 1, alpha, beta, True
                )

                board[i] = " "

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                if beta <= alpha:
                    break

        return best_score

# Find best move for AI
def best_move(board):
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            score = minimax(
                board, 0, -math.inf, math.inf, False
            )

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

# Main game
def play_game():
    board = [" "] * 9

    print("TIC TAC TOE")
    print("You are O")
    print("AI is X")

    while not is_game_over(board):

        # AI turn
        move = best_move(board)

        if move != -1:
            board[move] = "X"

        print("\nAI Move:")
        print_board(board)

        if is_game_over(board):
            break

        # Human turn
        while True:
            try:
                position = int(input(
                    "\nEnter your position (1-9): "
                ))

                if 1 <= position <= 9 and board[position - 1] == " ":
                    board[position - 1] = "O"
                    break
                else:
                    print("Invalid position! Try again.")

            except ValueError:
                print("Please enter a valid number.")

        print("\nYour Move:")
        print_board(board)

    # Final result
    winner = check_winner(board)

    if winner == "X":
        print("\nAI Wins!")
    elif winner == "O":
        print("\nYou Win!")
    else:
        print("\nGame Draw!")


# Start game
play_game()