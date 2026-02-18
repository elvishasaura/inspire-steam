#name: Elvis Mutuma
# Date : 18/02/2026
# Program to show dictionaries in python


car = {"Model" : "Audi"
        ,"Make" : "Q8",
        "Colour" : "Cherry",
          "Year" : "2025"}

print(car)

print(car["Model"])
print(car["Year"])

students = {"Alice": 24,
            "James": 18,
            "Mark": 22,
            "Susan" : 21}

for key in students:
    print(key)

for val in students.values():
    print(val)