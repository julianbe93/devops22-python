# `Exercise 3` Unicode

# How to write a euro sign can be found at [Currency Symbols](https://www.unicode.org/charts/PDF/U20A0.pdf). How to write emoji can be found at [emoji](https://unicode.org/emoji/charts/full-emoji-list.html), you can also check the formal charts for [symbols](https://www.unicode.org/charts/#symbols) you use either name or code: \N{money-mouth face}, or code \U0001F911

# Write a program that fulfills the specification

# 1. Let the user input a price, i.e Your new car cost: 1000000
# 2. Add a currency symbol (not dollar) to the input string. ie. Your new car cost [$]
# 3. Depending on the price, respond with a matching emoji (you decide which ones) i.e if cost below 50000 use one emoji, if is above another one

car_price = int(input("What is the price of your new car?: \u00a3"))

if (car_price > 50000):
    print('\U0001F631')
else:
    print('\U0001F44C')
