# `Exercise 3` Stack

# 1. Generate a list of lowercase a-z
# 2. Iterate through the alphabet and append each letter to a stack
# 3. Pop all elements and print on one line as a string


# 1.

import string

alphabet_string = string.ascii_lowercase
alphabet = list(alphabet_string)
print(alphabet)

# Martin
# list(string.ascii_lowercase)

# 2.

stack = []
for letter in string.ascii_lowercase:
    stack.append(letter)

# 3.

my_string = ""
while len(stack) > 0:
    my_string += stack.pop()

print(my_string)
