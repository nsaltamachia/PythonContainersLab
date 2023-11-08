# Exercise 1
students = ["Tom", "Jerry", "Homer", "Lisa"]
print(students[1])
print(students[-1])


# Exercise 2
foods = ("sandwich", "pizza", "pasta", "taco")
for food in foods:
    print(f"{food} is a good food.")


# Exercise 3
last_two_foods = foods[2:]
for food in last_two_foods:
    print(f"{food} is a good food.")
   

# Exercise 4
home_town = {
    "city": "Houston",
    "state": "Texas",
    "population": "2.28 million"
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}.")


# Exercise 5
for key, val in home_town.items():
    print(f"{key} = {val}")

    
# Exercise 6
cohort = []
students = ["Tom", "Jerry", "Homer", "Lisa"]
foods = ("sandwich", "pizza", "pasta", "taco")
for idx, student in enumerate(students):
    cohort.append({'student': student, 'fav_food':foods[idx]})
for entry in cohort:
    print(entry)


# Exercise 7
students = ["Tom", "Jerry", "Homer", "Lisa"]
awesome_students = [(f"{student} is awesome!") for student in students]
for student in awesome_students:
    print(student)  

# Exercise 8
foods = ("sandwich", "pizza", "pasta", "taco")
# a_containing_foods = []
# for food in foods:
#     if "a" in food:
#         a_containing_foods.append(food)
# print(a_containing_foods)

a_containing_foods = [food for food in foods if "a" in food]
print(a_containing_foods)