# Define the game board and player tokens
board = [' ' for _ in range(9)]
token = ['X', 'O']

# Function to print the game board
def print_board():
    for i in range(3):
        print(f"{board[i*3]:>5}{board[i*3+1]:>5}{board[i*3+2]:>5}")

# Function to check for a win
def check_winner():
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] != ' ':
            return board[i*3]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    if all(board):
        return 'D'
    return None

# Game loop
player = 0
while True:
    print_board()
    move = int(input(f"Player {token[player]} make a move (0-8): "))
    if move in range(9) and board[move] == ' ':
        board[move] = token[player]
        if winner := check_winner():
            print_board()
            print(f"Player {winner} wins!")
            break
        player = 1 - player
    else:
        print("Invalid move. Try again.")


