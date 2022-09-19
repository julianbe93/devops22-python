# `Exercise 4` import

# 3. Import & Create a custom module
#   1. Create a module named `calc.py`
#   2. Add a function add that takes arguments x, y and return x + y.
#   3. Import and use the function from `calc.py`

from random import randint
from calc import calculation_sheet
from math import sqrt

# 1. Import `sqrt` from `math`, calculate the sqrt of 16

print(sqrt(16))


# 2. Import `randint` from `random`, generate a random int 1 - 10

print(randint(1, 10))


# 3. Import & Create a custom module
#   1. Create a module named `calc.py`
#   2. Add a function add that takes arguments x, y and return x + y.
#   3. Import and use the function from `calc.py`

print(calculation_sheet(5, 2))
