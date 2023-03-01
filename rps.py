import sys
import random

# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


moves = ["rock", "paper", "scissors"]
move_dict = {
    ("rock", "paper"): False,
    ("paper", "scissors"): False,
    ("scissors", "rock"): False,
    ("paper", "rock"): True,
    ("scissors", "paper"): True,
    ("rock", "scissors"): True,
    ("rock", "rock"): True,
    ("paper", "paper"): True,
    ("scissors", "scissors"): True,
}


class Player:
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == moves[0]:
            self.my_move = moves[1]
        if self.my_move == moves[1]:
            self.my_move = moves[2]
        if self.my_move == moves[2]:
            self.my_move = moves[0]
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input("Rock, paper, scissors? > ").lower()
            if human_move in moves:
                return human_move
            print(f"The move {human_move} is invalid. Try again.")

    def learn(self, my_move, their_move):
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_win = 0
        self.p2_win = 0

    def who_wins(self, p1, p2):
        result = move_dict[(p1, p2)]
        if p1 != p2:
            if result is True:
                print("** PLAYER ONE WINS **")
                self.p1_win += 1
                print(f"Score: Player One {self.p1_win},"
                      + f"Player Two {self.p2_win} ")

            else:
                print("** PLAYER TWO WINS **")
                self.p2_win += 1
                print(f"Score: Player One {self.p1_win},"
                      + f" Player Two {self.p2_win}")
        if p1 == p2:
            print("** TIE **")
            print(f"Score: Player One {self.p1_win},"
                  + f" Player Two {self.p2_win}")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}. \n Opponent played {move2}.")
        self.who_wins(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def overall_score(self):
        if self.p1_win > self.p2_win:
            print("**** The winner is Player 1 ****\n "
                  + f"Score: Player One {self.p1_win}, "
                  + f"Player Two {self.p2_win}")
        if self.p1_win < self.p2_win:
            print("**** The winner is Player 2 ****\n "
                  + f"Score: Player One {self.p1_win}, "
                  + f"Player Two {self.p2_win}")
        if self.p1_win == self.p2_win:
            print("**** No winner this time, it's a tie! **** \n"
                  + f"Score: Player One {self.p1_win}, "
                  + f"Player Two {self.p2_win}")

    def play_game(self):
        print("Rock Paper Scissors, Go! \n")
        for round in range(3):
            print(f"Round: {round} --")
            self.play_round()
        if self.p1_win > self.p2_win:
            print("Player 1 won")
        if self.p1_win < self.p2_win:
            print("Player 2 won")
        self.overall_score()


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f"Please enter a valid input (Rock, Paper or Scissors) >")


def play_again():
    choise = valid_input("Press 'q' to quit or 'c' to continue > ", ['q', 'c'])
    if choise == "q":
        sys.exit("Goodbye!")


def choose_opponent():
    return valid_input("Please choose your opponent:\n"
                       "1 - Always rock\n"
                       "2 - Random\n"
                       "3 - Reflect\n"
                       "4 - Cycle\n",
                       ["1", "2", "3", "4"])


def game():
    while True:
        opponents = {
            "1": RockPlayer(),
            "2": RandomPlayer(),
            "3": ReflectPlayer(),
            "4": CyclePlayer()
        }
        p1 = HumanPlayer()
        p2 = opponents[choose_opponent()]
        game = Game(p1, p2)
        game.play_game()
        play_again()


if __name__ == "__main__":
    game()
