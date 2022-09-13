# `Exercise 1` Dataset

# Todays exercises requires that you generate test data. You can generate data in multiple ways i.e manually through loops, using `random` module or list comprehension. See examples in `8_data.py`.

# 1. Generate a list containing the numbers 1, 2, 3 to 100.

import random
one_to_hundred = [x for x in range(1, 101)]
# print(one_to_hundred)

# list(range(1, 101)) # Martin


# 2. Generate a list of all even numbers from 2 to 60

two_to_sixty = [x for x in range(2, 61)]
even_numbers = [x for x in two_to_sixty if x % 2 == 0]

# print(even_numbers)

# list(range(2, 61, 2)) # Martin

# 3. Generate a list of all odd numbers from 1 to 77
one_to_seventyseven = [x for x in range(1, 78)]
odd_numbers = [x for x in one_to_seventyseven if x % 2 == 1]

# print(odd_numbers)

# list(range(1, 78, 2)) # Martin

# 4. Generate a list of 100 numbers between 1 - 300
#   1. The numbers must be unique
#   2. The numbers are selected randomly(not unique)

# sample = unique, choices = not unique

# Unique
one_to_threehundred = random.sample(range(1, 301), 100)
# print(sorted(one_to_threehundred))


# from random import sample
# population = list(range(1, 301))
# hundred_numbers = sample(population, k=100)    # Martin

# Not Unique
one_to_threehundred_not_unique = random.choices(range(1, 301), k=100)
# print(one_to_threehundred_not_unique)


# from random import choices
# population = list(range(1, 301))
# hundred_numbers = choices(population, k=100)   # Martin


# 5. create a list containing five colors(not containing red)
#   1. Create a new list containing "red" and also add two colors by random with `choice`, `choices` or `sample` from the list.
#   2. Generate a list of random colors from the list of 3, the list should be of length 50.
#   3. Print the length of all three lists and the unique colors in each list


colors = ["green", "blue", "yellow", "black", "orange"]
new_colors = ["red"] + random.sample(colors, k=2)
# print(new_colors)
new_list = random.sample(new_colors, counts=[50]*len(new_colors), k=50)
# print(new_list)
# final_list = set(colors + new_colors + new_list)
unique_first = set(colors)
unique_second = set(new_colors)
unique_third = set(new_list)
print(
    f"First list of colors length: {len(colors)}\nUnique colors in first list: {len(unique_first)} {unique_first}\nSecond list of colors length: {len(new_colors)}\nUnique colors in second list: {len(unique_second)} {unique_second}\nThird list of colors length: {len(new_list)}\nUnique colors in third list: {len(unique_third)} {unique_third}")


# 5.1 Martin

# from random import sample
# colors = ["yellow", "blue", "green", "black", "white"]
# new_list = ["red"]
# new_list.extend(sample(colors, k=2))


# 5.2 Martin

# from random import sample, choice
# Part 1
#
#
