from tokenize import Number


number = int(input("Enter an integer: "))
if number % 2:
    print(f"Your number {number} is even")
else:
    print(f"Your number {number} is odd")
