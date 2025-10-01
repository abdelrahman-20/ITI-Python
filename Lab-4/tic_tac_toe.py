"""
Task Description:
design and implement a Tic-Tac-Toe game in Python using Object-Oriented Programming (OOP) concepts.
The game should allow the player to choose whether to play with a friend (human vs human) or against the computer (human vs computer).

Requirements:

1. Core Classes:
   - Player
     - Attributes: name, symbol (X or O).
     - Methods: make_move(board).
   - HumanPlayer (inherits from Player)
     - Implements make_move() by asking the user for input.
   - ComputerPlayer (inherits from Player)
     - Implements make_move() by choosing a move automatically (random or simple strategy).
   - Board
     - Attributes: 3x3 grid.
     - Methods: display(), update(position, symbol), check_winner(), is_full().
   - Game
     - Attributes: players, board, current_turn.
     - Methods: play(), switch_turns().

2. OOP Concepts to Use:
   - Encapsulation: Keep the board grid private, only modify it using methods.
   - Inheritance: HumanPlayer and ComputerPlayer inherit from Player.
   - Polymorphism: make_move() behaves differently depending on the type of player.
   - Special Methods: Implement __str__() for board display formatting.

3. Game Flow:
   - The program starts by asking:
     Do you want to play with a friend (1) or vs computer (2)?
   - If option 1 → two human players enter their names.
   - If option 2 → one human player enters their name, and the opponent is the computer.
   - Players take turns placing X or O on the grid.
   - After each move, the board is displayed.
   - The game checks if a player has won or if the board is full (draw).
   - Print the winner or “It’s a draw!” at the end.

Deliverables:
- A single Python script (tic_tac_toe.py).
- The game must run from the terminal using:
  python tic_tac_toe.py
- Code should be clean, well-structured, and commented.
- Every student must attach Code and screenshots of the game in BOTH modes (one with a friend and one against the computer) and place them inside a lab4 folder.
"""

# tizc_tac_toe.py

import random


# Player Base Class
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        """Abstract Method: Implemented Differently by HumanPlayer and ComputerPlayer"""
        raise NotImplementedError


# Human Player
class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                move = int(
                    input(f"{self.name} ({self.symbol}), enter your move (1-9): ")
                )
                if move < 1 or move > 9:
                    print("Invalid input! Please choose a number between 1 and 9.")
                    continue
                if board.update(move, self.symbol):
                    break
                else:
                    print("That spot is already taken. Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")


# Computer Player
class ComputerPlayer(Player):
    def make_move(self, board):
        print(f"{self.name} ({self.symbol}) is making a move...")

        # Getting Random Spot For The Computer To Play
        available_moves = board.get_available_moves()
        move = random.choice(available_moves)
        board.update(move, self.symbol)


# Board Class
class Board:
    def __init__(self):
        self.__grid = [" "] * 9

    # Display The Board in 2D
    def __str__(self):
        rows = [
            f" {self.__grid[0]} | {self.__grid[1]} | {self.__grid[2]} ",
            f" {self.__grid[3]} | {self.__grid[4]} | {self.__grid[5]} ",
            f" {self.__grid[6]} | {self.__grid[7]} | {self.__grid[8]} ",
        ]
        return "\n---+---+---\n".join(rows)

    # Display The Board in 2D
    def display(self):
        print(self.__str__())

    # Update The Board
    def update(self, position, symbol):
        if self.__grid[position - 1] == " ":
            self.__grid[position - 1] = symbol
            return True
        return False

    # Get Free Spots in The Board
    def get_available_moves(self):
        return [i + 1 for i, val in enumerate(self.__grid) if val == " "]

    # Check The Board For A Winner
    def check_winner(self):
        winning_combinations = [
            # Winning Rows
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            # Winning Columns
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            # Winning Diagonals
            (0, 4, 8),
            (2, 4, 6),
        ]

        for a, b, c in winning_combinations:
            if self.__grid[a] == self.__grid[b] == self.__grid[c] != " ":
                return self.__grid[a]  # return symbol of winner

        return None

    # Check For More Plays
    def is_full(self):
        return " " not in self.__grid


# Game Class
class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_turn = 0  # index of current player

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        print("\nGame Start!\n")
        self.board.display()

        while True:
            current_player = self.players[self.current_turn]
            current_player.make_move(self.board)
            self.board.display()

            winner = self.board.check_winner()
            if winner:
                print(f"🎉 {current_player.name} wins with '{winner}'!")
                break

            if self.board.is_full():
                print("It's a draw!")
                break

            self.switch_turns()


# Main Function
def main():
    print("Welcome to Tic-Tac-Toe!".center(50, "-"), "-" * 50)
    mode = input("Do you want to play with a friend (1) or vs computer (2)? ")

    if mode == "1":
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")
        player1 = HumanPlayer(name1, "X")
        player2 = HumanPlayer(name2, "O")

    elif mode == "2":
        name1 = input("Enter your name: ")
        player1 = HumanPlayer(name1, "X")
        player2 = ComputerPlayer("Computer", "O")

    else:
        print("Invalid option. Exiting game.")
        return

    game = Game(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
