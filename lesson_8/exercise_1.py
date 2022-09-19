# `Exercise 1` raise

# 1. Create a function that check if a variable is a float, if not it raises a TypeError("message")

def is_float(value):
    if not isinstance(value, float):
        raise TypeError("This is not a float")


my_var = 0
is_float(my_var)
