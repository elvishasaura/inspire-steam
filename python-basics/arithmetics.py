#name: Elvis Mutuma
# Date : 17/02/2026
# Program to perform arithmetic opertations

f_number = 12 # first number
s_number = 34 # second number
sum_number = f_number + s_number
diff_number = f_number - s_number
product_number = f_number * s_number
quotient_number = f_number / s_number


print("The sum of the numbers %d" %sum_number)
print("The quotient of the numbers %0.2f" %quotient_number)

#Modulus - remainder
print(7%3)

# Even and Odd numbers
for x in range(0,21):
    print(x)
    if(x%2 ==1):
        print("odd number")
    elif(x%2 ==0):
        print("even number")
    
    