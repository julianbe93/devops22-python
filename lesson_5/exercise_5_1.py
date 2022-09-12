# Exercise 5

# Instructions

# Todays exercises focus on String and it's built-in methods.


# Python
# firstname = "john"
# lastname = "smith"
# tele = "00468123456789"

# `Exercise 1` Basic usage

# 1. Print first, lastname and tele on the same line
# 2. Create a variable fullname
# 3. Assign to the new variable fullname, firstname and lastname separated with a space.
# 4. Print the length `len()` of fullname, firstname and lastname
# 5. Print a escape sequence `\n` so the first line contains fullname, and the second line tele.
# 6. Write the fullname and tele with the four different methods:
#    1. Only using print() and string concatenation i.e "firstname" + " " ..
#    2. Using f-string
#    3. Using format, i.e print('{}'.format(firstname))
#    4. Using printf ( % ) syntax, i.e print('A name %s' % firstname)

# 1
firstname = "john"
lastname = "smith"
tele = "00468123456789"
print(firstname + " " + lastname + " " + tele)

# 2 and 3?
fullname = firstname + " " + lastname
print(fullname)

# 4
print(len(fullname))

# 5
print(fullname + "\n" + tele)

# 6.1
print(fullname + " " + tele)

# 6.2
print(f'{fullname} {tele}')

# 6.3
print('{}'.format(fullname) + ' {}'.format(tele))

# 6.4
print('%s' % fullname + ' %s' % tele)
