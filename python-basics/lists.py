#name: Elvis Mutuma
# Date : 18/02/2026
# Program to show lists in python

friends = ["Elvis","Saka","Ehcico","kylie"]

print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends.append("Sophie")
print(friends)

new_freinds = ["Aisha","Kendall","Sheena","Jordan"]

print(len(new_freinds))
 # new list of students
students = friends + new_freinds

print(students)
students.pop()
print(students)

students.insert(4,"Piper")
print(students)

students.insert(9,"Valerie")
print(students)

students.extend("Ella")
print(students)

students.remove("Saka")
print(students)

new_students = students.copy
print(new_students)