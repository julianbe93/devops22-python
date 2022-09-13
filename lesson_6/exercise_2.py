# `Exercise 2` Name Counter


from audioop import reverse
from collections import Counter
from enum import unique
from operator import itemgetter
from random import sample
import random

# 1. Generate a list with 100 elements, i.e["johan", "lisa", "johan", "tove"...]

name_list = sample(['John', 'Amanda', 'Juan', 'Lisa',
                   'Miguel'], counts=[100, 100, 100, 100, 100], k=100)

sorted_names = sorted(name_list)

# 2. Count the names i.e('lisa', 1), ('johan', 2)

c = Counter(name_list)
print(c)

# 3. Print the top 3 most popular names

print(c.most_common(3))

# 4. Print the least popular name[s]

print(c.most_common()[:3:-1])


# 5. Print all unique names
#     1. In alphabetical order

unique_names = set(name_list)
print(sorted(unique_names))

#     2. Shuffled
random.shuffle(name_list)
print(set(name_list))

#     3. In reversed alphabetical order

unique_names_reversed = sorted(unique_names, reverse=True)
print(unique_names_reversed)
