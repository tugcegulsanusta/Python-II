#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


import random
moves = ['rock', 'paper', 'scissors']
move_dict = {("rock", "paper"):False,
             ("paper", "scissors"):False,  
             ("scissors","rock"):False,
             ("paper","rock"):True,
             ("scissors", "paper"): True,
             ("rock", "scissors"): True,
             ("rock","rock"): True,
             ("paper", "paper"): True,
             ("scissors", "scissors"): True
             }


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        human_move = input("Rock, paper, scissors? > ").lower()
        while human_move not in moves:
            human_move = input("Rock, paper, scissors? > ").lower()
        return human_move
    
class Game:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_win = 0
        self.p2_win = 0

    def who_wins(self, p1, p2):
        result = move_dict[(p1, p2)]
        if p1 != p2:
            if result == True:
                print("** PLAYER ONE WINS **")
                self.p1_win += 1
                print (f"Score: Player One {self.p1_win}, Player Two {self.p2_win}")
                
            else:
                print("** PLAYER TWO WINS **")
                self.p2_win += 1
                print (f"Score: Player One {self.p1_win}, Player Two {self.p2_win}")
        if p1 == p2:
            print("** TIE **")  
            print (f"Score: Player One {self.p1_win}, Player Two {self.p2_win}")


    
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}. \n Opponent played {move2}.")
        self.who_wins(move1, move2)               
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


    def play_game(self):
        print("Rock Paper Scissors, Go! \n" )
        for round in range(3):
            print(f"Round: {round} --")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()