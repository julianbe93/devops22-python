# `Exercise 3` Return

# 1. Create a function that returns a integer

def number():
    print(int())


number()


# 2. Create a function that returns a tuple with (x, y) value

def tuple(x, y):
    x = 10
    y = 5
    print((x, y))


tuple(1, 2)

# 3. Create a function that returns a boolean value


def boolean_value():
    print(2 > 1)


boolean_value()


# 4. Create a function that returns a float

def float_value():
    print(float(3.2 - 3))


float_value()


# 5. Create a function that has `firstname` and `lastname` as parameters and returns fullname.

def fullname(firstame="John", lastname="Wayne"):
    print(firstame, lastname)
    return (fullname)


fullname("Juan", "Miguel")


# 6. Create a function that calculates the area of a rectangle and returns the result

def area_rectangle(length, width):
    area = length * width
    print(area)


area_rectangle(4, 6)


# 7. Create a function that expects a list as argument, the list should contain integers and the function should return the sum of all elements in the list.

def list_math(list=[]):
    sum_1 = sum(list)
    print(sum_1)


list_math([1, 2, 10])


# 8. Create a function that repeats a word multiple time, `word` and `repeat` is used as parameters. If the word is hello and repeat is 3, it will print hello three times.

def multiple_time(word="Hello", repeat=3):
    print(word * repeat)


multiple_time()
