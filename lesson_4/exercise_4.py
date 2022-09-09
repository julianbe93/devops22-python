start_integer = int(input("What is the first integer?: "))
stop_integer = int(input("What is the last integer?: "))

total = 0
for i in range(start_integer, stop_integer):
    print(i)
    total += i

print(f"the sum of all integers is {total} ")
