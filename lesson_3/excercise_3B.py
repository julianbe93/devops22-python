from operator import itemgetter
persons = []

name_1 = input("Please enter name for person 1: ")
print(name_1.capitalize())
age_1 = int(input("Please enter age for person 1: "))
print(age_1)
shoe_size_1 = float(input("Please enter shoe size for person 1: "))
print(shoe_size_1)
person_1 = (name_1, age_1, shoe_size_1)
persons.append(person_1)

name_2 = input("Please enter name for person 2: ")
print(name_2.capitalize())
age_2 = int(input("Please enter age for person 2: "))
print(age_2)
shoe_size_2 = float(input("Please enter shoe size for person 2: "))
print(shoe_size_2)
person_2 = (name_2, age_2, shoe_size_2)
persons.append(person_2)

name_3 = input("Please enter name for person 3: ")
print(name_3.capitalize())
age_3 = int(input("Please enter age for person 3: "))
print(age_3)
shoe_size_3 = float(input("Please enter shoe size for person 3: "))
print(shoe_size_3)
person_3 = (name_3, age_3, shoe_size_3)
persons.append(person_3)

sorted_shoe_size = sorted(persons, key=itemgetter(1))
sorted_age = sorted(persons, key=itemgetter(2))

oldest = sorted_age[2]
median_size = sorted_shoe_size[1]


print(
    f"The oldest person is: {oldest[0].capitalize()}, who has shoe size: {oldest[2]}")
print(
    f"The person withe the median shoe size is: {median_size[0].capitalize()}, who is: {median_size[1]} years old")

searches = {
    "age": {
        str(age_1): person_1,
        str(age_2): person_2,
        str(age_3): person_3
    },
    "shoe": {},
    "name": {}
}
prop, value = input("Enter prop value: ").split(" ")
print(searches[prop][value])
