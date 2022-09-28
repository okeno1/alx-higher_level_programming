#!/usr/bin/python3
def best_score(a_dictionary):
    maximum = 0
    winner = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > maximum:
                maximum = value
                winner = key
    return winner
