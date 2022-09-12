# `Exercise 4` Extra

# Write a program that handles salary negotiations. The user is the employee and the boss is your program.

# 1. The boss tells the user it's current salary and currency
# 2. The employee ask for more money with an input. I.e 2000 more
# 3. The boss calculates the percentage salary increase and respond with a emoji. And always respond NO to the initial proposal.
# 4. The employee ask again for another amount i.e 1800
# 5. The boss calculates the percentage and respond yes or no, you decide which criteria the boss uses. 4 and 5 iterates in a loop until the employee quit or the boss accept the amount.


salary = int(5000)
currency = "\u00a3"
current_salary = currency + format(salary)

desired_raise = int(input(
    f'Me: My current salary is {current_salary} and I would like a raise of: \u00a3'))
salary_raise_1 = int(desired_raise) / int(salary)
salary_raise_2 = salary_raise_1 * 100
print("Boss: \U0001F937. Can't do that, sorry. Try again...")

desired_raise_2 = int(input(
    "Boss: Please be more reasonable this time, how much of a raise do you want? \nMe: \u00a3"))
condition = True
while condition == True:
    boss_percentage = int(desired_raise_2) / int(salary)
    boss_percentage_2 = boss_percentage * 100
    if boss_percentage_2 <= 0.15 * 100 and boss_percentage_2 < salary_raise_2:
        print("Boss: That is reasonable...\nBoss: We have a deal \U0001F91D")
        break
    else:
        desired_raise_2 = int(input("Boss: Think again... \nMe: \u00a3"))


"""
salary = 10000
currency = 'SEK'
print(f"Your current salary is {salary} {currency}")

initial_increase = initial_increase / salary * 100
"""
