#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations

class CodeBreaker():

    """Defines the person that tries to find the code"""

    def __init__(self, dimension = 4, nbr_color = 6):
        self._nbr_color = nbr_color
        self._dimension = dimension
        self._S = sorted(list(set(permutations( list(range(1,nbr_color+1)) * dimension, dimension))))
        self._S_static =  sorted(list(set(permutations( list(range(1,nbr_color+1)) * dimension, dimension))))


    def shrink_possibility(self, guess, result):
        self._S = sorted([ possibility for possibility in self._S if self.verify_guess(guess, possibility) == result ])


    def shrink_possibility_list(self, guess, result):
        return [ possibility for possibility in self._S if self.verify_guess(guess, possibility) == result ]


    def verify_guess(self, guess, solution):
        result = {"good" : 0, "misplaced" : 0, "wrong" : 0 }
        solution2 = list(solution)
        for i,color in enumerate(guess):
            if color == solution[i]:
                solution2.remove(color)
                result["good"] += 1

        result["misplaced"] = len([ color for color in solution2 if color in guess ])
        result["wrong"] = self._dimension - result["good"] - result["misplaced"]

        return result


    def result_tuple_to_dict(self,result):
        return {"good" : result[0], "misplaced" : result[1], "wrong" : result[2] }

    def define_possibility(self,guess):
        possible_return = set()
        for possibility in self._S:
            possible_result = self.verify_guess(guess,possibility)
            possible_return.add((possible_result["good"],possible_result["misplaced"],possible_result["wrong"]))
        return possible_return

    def make_guess(self, nbr_try):
        if nbr_try == 1:
            return (1,1,2,2)
        elif len(self._S) == 1:
            return self._S[0]
        else:
            minimum = len(self._S)
            for possibility in self._S_static:
                min_partial = max([ len(self.shrink_possibility_list(possibility, self.result_tuple_to_dict(possible_return))) for possible_return in self.define_possibility(possibility) ])
                inside_s = False
                if min_partial < minimum:
                    minimum = min_partial
                    guess = possibility
                    inside_s = True if guess in self._S else False
                elif (min_partial == minimum) and (not inside_s) and (possibility in self._S):
                    minimum = min_partial
                    guess = possibility
                    inside_s = True
            return guess


