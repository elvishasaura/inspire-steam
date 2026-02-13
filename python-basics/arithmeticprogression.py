# Name : Elvis Mutuma
# Date : 13/02/2026
# Program to calculate arithmetic progression

#calculating nth term

a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
d = int(input("Enter the common difference :"))

nth_term = a + (n-1)*d
Sn = (n/2)*(2*a + (n-1)*d)
print(f"The nth term is: {nth_term}")
print(f"the sum of numbers is: {Sn}")