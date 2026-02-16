#name: Elvis Mutuma
# Date : 16/02/2026
# Program to calculate income tax

salary = int(input("Enter your gross salary:"))
if salary < 50000:
    tax = (2.5/100)*salary
    net_salary = salary - tax


print(f"Gross salary = {salary}")    
print(f"Net salary = {net_salary}")
print(f"Tax = {tax}") 

salary = int(input("Enter your gross salary"))
if salary>50000 and salary<100000:
    tax = (4.5/100)*salary
    net_salary = salary - tax 

print(f"Gross salary:{salary}")    
print(f"Tax:{tax}") 
print(f"Net salary:{net_salary}")  

salary = int(input("Enter your gross salary"))
if salary>100000:
    tax = (7.5/100)*salary
    net_salary = salary - tax

print(f"Gross salary:{salary}")    
print(f"Tax:{tax}") 
print(f"Net salary:{net_salary}") 
