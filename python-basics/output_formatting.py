#name: Elvis Mutuma
# Date : 17/02/2026
# Program to format output in different styles

name = "Elvis Mutuma"
weight = "65" #weight in kgs
fav_team = "Arsenal"
height = "187" #height in cms

# 1. format using printf(f"{}")

print(f"My name is {name} and I weigh {weight}kgs")

# 2. using f string
msg = f"My name is {name} and I support {fav_team}"
print(msg)

# 3. Using {} and .format()

print("My name is {0} and I am {1} cms tall".format(name,height))

# 4. Using output specifiers %s

print("I support %s" %fav_team)
