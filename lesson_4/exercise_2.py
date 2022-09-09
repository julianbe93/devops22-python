from atexit import register


username = input("What is your name?: ")

registered_names = ("Ozzy", "Amanda", "Zakk", "Natalia", "Gus")

if username in registered_names:
    print(f"Welcome {username} your are on the list")
else:
    print(f"Sorry, you are not on the list")
