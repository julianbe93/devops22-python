# `Exercise 3` Stack

# 1. Generate a list of lowercase a-z
# 2. Iterate through the alphabet and append each letter to a stack
# 3. Pop all elements and print on one line as a string


# 1.

import string

alphabet_string = string.ascii_lowercase
alphabet = list(alphabet_string)
print(alphabet)

# 2.

stack = []
stack.append(alphabet[0:27])
print(stack)

stack.pop()
print(f"{stack}")
