def print_board(board):
    """ Print the Tic-Tac-Toe board """
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board, player):
    """ Check if the player has won """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    moves_left = 9

    while moves_left > 0:
        print_board(board)
        player = players[current_player]
        print(f"Player {player}'s turn")
        row = int(input("Enter row number (0, 1, 2): "))
        col = int(input("Enter column number (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = player
            moves_left -= 1
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            current_player = (current_player + 1) % 2
        else:
            print("That cell is already taken. Try again.")

    if moves_left == 0:
        print_board(board)
        print("It's a tie!")

if __name__ == "__main__":
    main()
