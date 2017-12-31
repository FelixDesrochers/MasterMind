#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codemaker import *
from functions import *
from sys import exit

#Defining the parameters of the game
nbr_life = 8
dimension = 4
nbr_color = 6
nbr_try = 1

#Define the codemaker
GameMaster = CodeMaker(code = (6,4,5,5))

#Defining the process of the game
while nbr_try < nbr_life:

    print("\nSolution : {}".format(GameMaster._code))
    print("\n{} try".format(nbr_try))

    #Make the guess
    guess = input("Enter a guess: ").split()
    guess = tuple([int(i) for i in guess])
    guess = verify_input(guess, dimension, nbr_color)

    #Verify the guess and display a message to the player
    result = GameMaster.verify_guess(guess)
    display_result(result)

    if result["good"] != dimension:
        nbr_try += 1
    else:
        print("Victory in {} tries".format(nbr_try))
        exit(0)

print("You weren't able to trick the codemaker.. Best luck next time")
print("Vous n'avez pas réussi à déjouer le code maker... Meilleur chance la prochaine fois!")
exit(0)
