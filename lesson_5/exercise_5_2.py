# Exercise 5

# Python
# firstname = "john"
# lastname = "smith"
# tele = "00468123456789"

# `Exercise 2` Slice

# Slice can be used to get a substring, i.e to get all but last letter my_string[:-1], to get all except the first letter my_string[1:], to get three first letters my_string[:3]

# Docs about [slice](https://docs.python.org/3/library/functions.html#slice)

# 1. Use slice to get the first 5 characters i fullname
# 2. Use slice to get all characters except the first and last one
# 3. Use slice to get every other character, i.e abcdef would print ace. Print the result in uppercase.
# 4. Use slice to print a word backwards.
# 5. Use slice to get the 5th character

firstname = "john"
lastname = "smith"
tele = "00468123456789"

fullname = firstname + " " + lastname

# 1
print(fullname[0:4])

# 2
print(fullname[1:-1])

# 3
upper_case = fullname.upper()
print(upper_case[::2])

# 4
print(fullname[::-1])

# 5
print(fullname[4:5])
