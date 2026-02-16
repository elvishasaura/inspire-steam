#name: Elvis Mutuma
# Date : 16/02/2026
# Program to calculate geometric progression


#Elvis' attempt on Geometric Progression
a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
d = int(input("Enter the common difference :"))
r = int(input("Enter the common ratio:"))

nth_term = a*(r**(n-1))
print(f"The nth_term is: {nth_term}")

Sn = (a*((r**n)-1)) / (r-1)
print(f"The sum of the numbers is: {Sn}")