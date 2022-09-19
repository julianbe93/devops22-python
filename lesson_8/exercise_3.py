# `Exercise 3` try/except

# 1. Create a function that uses try / except
# 2. The function should have the parameters x, y
# 3. The function should return x/y
# 4. If the user provide a y = 0, it should except the error and print 'Division by zero is not allowed'
# 5. If the argument y is a string, it should raise a TypeError

def try_except():
    try:
        x = int(input("Write a number: "))
        y = int(input("Write a number that is gonna divide the first one: "))
        a = x / y
        print(a)
        pass
    except ZeroDivisionError:
        print("Divison by 0 is not allowed")
        return try_except()
    except ValueError:
        print("This is not a valid integer")
        return try_except()


try_except()
