# name:Elvis Mutuma
# date:18/2/2026
# Program to show tuples in python
# tuples of fruits

fruits = ("Avocado","Apple","Kiwi","Banana","Grapes","Pineapples")

print(len(fruits))
print(fruits[0])
print(fruits[5])
print(fruits[-1])
print(fruits[-5])

# error -> fruits.append("Guava")

fruits_list = list(fruits)
fruits_list.append("Guava")
print(fruits_list)