from os import system
from time import sleep


# Functions:
def create_board():
    return [[y for y in range(x, x + 3)] for x in range(1, 10, 3)]


# Console function
def clean_screen():
    system("cls")


def print_board(board, symbols, count):
    clean_screen()

    print(f"Player one -> [{symbols['Player one']}] VS Player two -> [{symbols['Player two']}]\n")
    print(f"Total turns: {count}\n")

    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}\n")


def get_player_turn(player, symbols, board, count):
    print_board(board, symbols, count)

    number = int(input(f"{player} choose a number: "))

    for row in range(3):
        for col in range(3):
            if board[row][col] == number:
                board[row][col] = symbols[player]
                return

    print("\nERROR: Wrong number! Try again!")
    sleep(2.0)
    get_player_turn(player, symbols, board, count)


def check_winner(player, board):
    if board[0][0] == board[0][1] == board[0][2] or \
            board[1][0] == board[1][1] == board[1][2] or \
            board[2][0] == board[2][1] == board[2][2] or \
            board[0][0] == board[1][0] == board[2][0] or \
            board[0][1] == board[1][1] == board[2][1] or \
            board[0][2] == board[1][2] == board[2][2] or \
            board[0][0] == board[1][1] == board[2][2] or \
            board[0][2] == board[1][1] == board[2][0]:
        return player
    return False


# Main:
print("Hi, this is my Tic Tac Toe game! Enjoy it :)\n")

while True:
    board = create_board()
    total_turns = 0

    players_symbols = {
        "Player one": input("Player one choose symbol [X or O]: "),
        "Player two": input("Player two choose symbol [X or O]: ")
    }

    turn = "Player one"

    while True:
        get_player_turn(turn, players_symbols, board, total_turns)
        total_turns += 1

        winner = check_winner(turn, board)

        if winner:
            clean_screen()
            print(f"{winner} wins in {total_turns} turns!\n")
            break

        if total_turns == 9:
            clean_screen()
            print("Draw!\n")
            break

        turn = "Player two" if turn == "Player one" else "Player one"

    again = input("Do you want to play again [Y] or [N]?: ")
    if again != "Y" : break
    clean_screen()
