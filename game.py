#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codemaker import *
from codebreaker import *
from functions import *
from sys import exit


class Game():

    """Defines the game and its rules"""


    def __init__(self, nbr_life=8, dimension=4, nbr_color=6, nbr_try=0):

        self._nbr_life = nbr_life
        self._dimension = dimension
        self._nbr_color = nbr_color
        self._nbr_try = nbr_try

    def define_codemaker(self):
        return CodeMaker()

    def define_codebreaker(self):
        return CodeBreaker()

    def display_result(self, result):
        print("""You have:
        {0} good color at the right position,
        {1} good color at the wrong position
        {2} color(s) that are not in the code\n""".format(result["good"], result["misplaced"], result["wrong"]))

    def verify_input(self, guess):
        while (type(guess) != tuple) or (len(guess) != self._dimension) or (max(guess) > self._nbr_color) or (min(guess) <= 0):
            guess = input("The present guess is invalid. Enter a valid one: ")
            guess = tuple( [int(i) for i in guess.split() ] )

        return guess


    def complete_game(self):

        #Define the code maker
        code_maker = self.define_codemaker()
        code_breaker = self.define_codebreaker()

        while self._nbr_try < self._nbr_life:
            self._nbr_try += 1
            print("\n{} try".format(self._nbr_try))

            #See the guess made by the code breaker
            breaker_guess = code_breaker.make_guess(self._nbr_try)
            print(code_breaker._S)
            print("Secret code: {}".format(code_maker._code))
            print("Breaker guess: {}".format(breaker_guess))


            #Make the guess
            #guess = input("Enter a guess: ").split()
            #guess = tuple([int(i) for i in guess])
            #guess = self.verify_input(guess)
            guess = breaker_guess

            #verify the guess
            result = code_maker.verify_guess(guess)
            self.display_result(result)
            code_breaker.shrink_possibility( breaker_guess, result)

            if result["good"] == self._dimension:
                print("Victory in {} tries".format(self._nbr_try))
                break
                #exit(0)


        print("You weren't able to trick the codemaker.. Best luck next time")
        #exit(0)


