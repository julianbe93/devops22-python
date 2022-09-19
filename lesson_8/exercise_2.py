# `Exercise 2` input validation

# 1. Create a program that takes input and convert it to a integer
# 2. If it's not possible to convert it to a integer the program should print `Sorry, not an int`
# 3. If the input fail to convert to a int, the program should retry the input
# 4. If the number is even, raise a Exception('Even numbers is not allowed')


# number_question = float(input("Enter a number: "))
# print(int(number_question))


# def integer_convertor(text):
#     number = None
#     while True:
#         try:
#             number = int(float(input(text)))
#             break
#         except ValueError:
#             print("Sorry, not an int")
#         except:
#             raise Exception
#     if (number % 2 == 0):
#         print("Even numbers is not allowed!")
#         return integer_convertor(text)
#     else:
#         return number


# my_number = int(integer_convertor("Enter a number: "))
# print(f'result: {int(my_number)}')


#     raise Exception
# if (number % 2 == 0):
#     print("Even numbers is not allowed!")
# else:
# ?????????????????????????


# Martin

def int_input():
    try:
        return int(input("Write an integer: "))
    except:
        print("Sorry, not an int")
        return int_input()


def even_input():
    number = int_input()
    if not number % 2:
        raise Exception('Even numbers are not allowed')
    return number


even_input()


# -> int | Unknown
