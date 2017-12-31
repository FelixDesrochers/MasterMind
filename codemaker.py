#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class CodeMaker():

    """This class defines the codemaker i.e. the person that creates the code to break and that determines if the guesse is goo or not"""

    def __init__(self, code=None, dimension = 4, nbr_color = 6):

        self._dimension = dimension
        self._nbr_color = nbr_color

        if code:
            while (type(code) != tuple) or (len(code) != dimension) or (max(code) > nbr_color):
                code = input("Enter a valid code: ")
            self._code = code
        else:
            self._code = tuple([ randint(1,nbr_color) for i in range(dimension) ])


    def verify_guess(self, guess):
        result = {"good" : 0, "misplaced" : 0, "wrong" : 0 }
        solution = list(self._code)
        for i,color in enumerate(guess):
            if color == self._code[i]:
                solution.remove(color)
                result["good"] += 1

        result["misplaced"] = len([ color for color in solution if color in guess ])
        result["wrong"] = self._dimension - result["good"] - result["misplaced"]

        return result


    def verify_victory(self, guess):
        result = self.verify_guess(guess)
        if result["good"] == self._dimension:
            print("Victoire!!")
            return True

        else:
            return False

    def __repr__(self):
        return "CodeMaker: code({0}), dimension({1}), nbr_color({2})".format(self._code, self._dimension, self._nbr_color)
