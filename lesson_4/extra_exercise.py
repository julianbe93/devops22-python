# 1. Skriv ett program som hälsar användaren 10 gånger
"""
username = input("What is your name?: ")
amount = int(10)
for i in range(int(amount)):
    print(f"Hello {username}")
"""

# 2. Skriv ett program (med for-loop) som skriver ut följande:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

"""
numbers = int(9)

for i in range(1, numbers+1):
    for x in range(1, i+1):
        print(i, end="")
    print()
"""

# 3. Skriv ett program som låter användaren gissa vilket tal du tänker på tills användaren
# gissar rätt.
# Talet har du hårdkodat in i programmet och gissningen från användaren hämtas in via
# input gång på gång tills dess att gissning == input.
# Exempel-output:
# $ python my_program.py
# Enter an integer: 100
# Wrong, it’s lower.
# Enter an integer: 12
# Wrong, it’s higher.
# Enter an integer: 42
# Congratulations, you’re correct!

"""

number = int(23)

while True:
    user_guess = int(input("Enter an integer: "))
    if int(user_guess) == number:
        print("Congratulations, you\'re correct!")
    if int(user_guess) < number:
        print("Wrong it\'s higher.")
    if int(user_guess) > number:
        print("Wrong it\'s lower.")
    if int(user_guess == int(number)):
        break

"""

# 4. Skriv ett program som loopar över en lista innehållandes olika tal. Om programmet stöter
# på ett ojämnt tal skrivs orden “Not allowed!” ut och loopen avbryts.

"""
number = [2, 4, 6, 8, 10, 3, 5, 11]
for number in number:
    print(number)
    if number % 2:
        print("Not allowed")
        break
"""

# 5. Genom att använda en for-loop, skriv ett program som för varje tal i second_list, hämtar
# talet och dess position i first_list och skriver resultatet som en lista av tupler.
# Exempel:
# first_list = [3, 7, 9, 2, 6]
# second_list = [2, 3, 6, 7, 9]
# Output: [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]

"""
first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]

result = []
for number in second_list:
    result.append((number, first_list.index(number)))
print(result)
"""

# 6. Upprepa uppgiften ovan, men använd denna gång list comprehension för att lösa problemet.

"""
first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]

result = [(x, first_list.index(x)) for x in second_list]
print(result)
"""

# 7. Du har följande lista på frukter:
# fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
# Skriv ett program som frågar användaren efter hur många platser för frukt hen har i sin
# korg, och sedan fyller du denna korg(en lista) med frukter genom att loopa igenom
# frukt-listan tills dess att korg-listan är full.
# Output-exempel:
# My_basket = ['apple', 'orange', 'pear', 'banana', 'grapes', 'apple',
#            'orange', 'pear']


fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
basket = []
amount = int(input("How many fruits fit in your basket?: "))

for i in range(amount):
    basket.append(fruits[i % len(fruits)])
print(basket)
