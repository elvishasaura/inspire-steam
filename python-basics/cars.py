#name: Elvis Mutuma
# Date : 23/02/2026
# Program to show classes in python

class Car():
    # attributes of the car
    def __init__(self,model,make,colour,year):
        self.model = model
        self.make = make
        self.colour = colour
        self.year = year

    # print car details
    def print_details(self,model,make,colour,year):
        print(f"{make} {model} of colour {colour} was manufactured in the year {year}")



# instantiate a class object

my_car = Car("Atenza","Mazda","Black","2025")
dads_car = Car("Landcruiser","Toyota","Grey","2024")

my_car.print_details("Atenza","Mazda","Black","2025")
    
    
