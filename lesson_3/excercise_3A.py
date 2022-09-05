X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5",
             "Bella": "Klockgatan 1",
             "Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

# 1 och 2
print(type(X), type(Y), type(addresses))

# 3
print(addresses["Bella"])

# 4
addresses["Daniel"] = "Prinsgränd 2"
print(addresses["Daniel"])

# 5
print(len(addresses))

# 5.1
last_key = sorted(addresses)[-1]
print(addresses[last_key])


# 5.2
addresses = {v: k for k, v in addresses.items()}

first_value = sorted(addresses)[0]
print(addresses[first_value])


# 6
print(type(cars))

# 7
print(cars[X])


# 8 print(cars[Y]) ERROR för att det inte finns 4 values

# 9
print(cars.sort())  # Returns NONE
print(cars[0])  # Returns BMW


# 10
cars_2 = cars[0:len(cars)]
cars.append("Saab")
print(cars, cars_2)


# 10.1
cars_3 = cars[:]

# 10.2
cars *= 2
print(sorted(cars, reverse=True))

# 10.3
unique_cars = set(cars)
print(unique_cars)

# 11
print(type(numbers1), type(numbers2))

# 12
print(numbers1)
print(numbers2)
#SVAR: INTEGERS

# 13 Itersection är 2, 3
print(numbers1 & numbers2)

# 14 UNION är 1, 2, 3, 4, 6, 7
print(numbers1 | numbers2)

# 15 Symmetriska differensen är 1, 4, 6, 7
print(numbers1.symmetric_difference(numbers2))
