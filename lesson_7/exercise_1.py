# `Exercise 1` Functions

from audioop import reverse
from ctypes.wintypes import WORD
import string

# 1.Create a function with name `do_nothing`
#    1. The function should have a `pass`
#    2. Call the function from your code


def do_nothing():
    pass


do_nothing()


# 2. Functions getting started:

# 2.1 Create a function that prints `hello world`

def hello_world():
    print("Hello World")


hello_world()

# 2.2 Create a function that prints the result from `1 == 1.0`


def result():
    print(1 == 1.00)


result()

# 2.3 Create a function that prints the alphabet in reverse order

alphabet = (string.ascii_lowercase)


def reverse_alphabet():
    print(alphabet[::-1])


reverse_alphabet()


# 3 Functions with arguments

# 3.1 Create a function that prints `hello name` with name as a parameter

def greeting(name, phrase="hello"):
    print(f'{phrase} {name}')


greeting("Julian")


# 3.2 Create a function that prints a string in capital letters, with `word` as a parameter

def capital_string(word):
    print(word.upper())


capital_string("hello")

# 3.3 Create a function that prints numbers between 1 and `stop`, where stop is a parameter


# def numbers():
#     stop = 11
#     for i in range(1, stop):
#         print(i)


# numbers()

def numbers(stop, start=1):
    for x in range(start, stop):
        print(x)


numbers(11)
