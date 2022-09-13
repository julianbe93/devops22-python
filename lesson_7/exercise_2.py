# `Exercise 2` Default Arguments

# # 1. Create a function that prints 1 to 10 by default, i.e `start = 1` `stop = 11` and uses a range in the function block.
from audioop import reverse
import string


def numbers(stop=11, start=1):
    for x in range(start, stop):
        print(x)


numbers()


# 2. Create a function that by default prints a string, if `reverse = True` is used as argument the string is printed in reverse.


def string_reversed(phrase="Hello", reverse=True):
    if reverse == True:
        print(phrase[::-1])


string_reversed()


# 3. Call the same function with and without reverse

def string_notreversed(phrase="Hello", reverse=False):
    if reverse == False:
        print(phrase)


string_notreversed()

"""
WHY NOT THIS?
"""

# def string_notreversed(phrase="Hello"):
#     print(phrase)


# string_notreversed()
