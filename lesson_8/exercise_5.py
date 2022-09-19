# `Exercise 5` lambda

# 1. Create a list with numbers from 1 - 10
# 2. Create a lambda expression that add 1 to each element: `lambda x: x + 1`
# 3. Apply the lambda on each element in the list with map(your_lambda, your_list)
# 4. Print a list from 3

one_to_ten = list(range(1, 11))
print(list(map(lambda x: x + 1, one_to_ten)))


# my_list = list(map(xy, one_to_ten))

# print(my_list[2:-1])

# with_lambda = sum(filter(lambda x: x + 1, one_to_ten))

# # list_with_lambda = one_to_ten
# # print(sum(filter(lambda x: x + 1, list_with_lambda)))

# # Trick with map and join


# def print_map(b):
#     print('\n'.join(map(str, b)))


# print_map(with_lambda)
