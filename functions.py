#!/usr/bin/env python
# -*- coding: utf-8 -*-

#define decorator who can verify the type of the variable of a function
def control_types(*a_args, **a_kwargs):
    """On attend en paramètres du décorateur les types souhaités. On accepte
    une liste de paramètres indéterminés, étant donné que notre fonction
    définie pourra être appelée avec un nombre variable de paramètres et que
    chacun doit être contrôlé"""

    def decorateur(fonction_a_executer):
        """Notre décorateur. Il doit renvoyer fonction_modifiee"""
        def fonction_modifiee(*args, **kwargs):
            """Notre fonction modifiée. Elle se charge de contrôler
            les types qu'on lui passe en paramètres"""

            # La liste des paramètres attendus (a_args) doit être de même
            # Longueur que celle reçue (args)
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas égal " \
                        "au nombre reçu")
            # On parcourt la liste des arguments reçus et non nommés
            for i, arg in enumerate(args):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type " \
                            "{1}".format(i, a_args[i]))

            # On parcourt à présent la liste des paramètres reçus et nommés
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {0} n'a aucun type " \
                            "précisé".format(repr(cle)))
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("l'argument {0} n'est pas de type" \
                            "{1}".format(repr(cle), a_kwargs[cle]))
            return fonction_a_executer(*args, **kwargs)
        return fonction_modifiee
    return decorateur


#Define a function to verify the input by the player
def verify_input(guess, dimension, nbr_color):
    while (type(guess) != tuple) or (len(guess) != dimension) or (max(guess) > nbr_color) or (min(guess) <= 0):
        guess = input("The present guess is invalid. Enter a valid one: ")
        guess = tuple( [int(i) for i in guess.split() ] )

    return guess

#Define a function to display a message depending on the result of the guess
def display_result(result):
    print("""You have:
    {0} good color at the right position,
    {1} good color at the wrong position
    {2} color(s) that are not in the code""".format(result["good"], result["misplaced"], result["wrong"]))
