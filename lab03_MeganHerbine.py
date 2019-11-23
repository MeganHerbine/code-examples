#Megan Herbine CSCI-181-01
#Lab calculating value of change, volume and surface area of a sphere,
#molecular weight of a hydrocarbon, area of a triangle, and a Gregorian epact

def q01():
    print("This is question 1 of lab03"); #Value of some change in dollars
    print("Please enter the count of each type of coin:")
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickels = float(input("Nickels: "))
    pennies = float(input("Pennies: "))
    total = quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01
    print("The total value of your change is $", total,"\n")

import math
    
def q02():
    print("This is question 2 of lab03"); #Volume and surface area of a sphere
    print("Please enter the radius of the sphere:")
    radius = eval(input("Radius: "))
    volume = (4/3)*math.pi*(radius)**3
    s_area = 4*math.pi*(radius)**2
    print("The volume of the sphere is ", volume," cubic units.")
    print("The surface area of the sphere is ", s_area," square units.\n")

def q03():
    print("This is question 3 of lab03"); #Molecular weight of a hydrocarbon
    print("Please enter the count of each type of molecule:")
    hydrogen = eval(input("Hydrogen atoms: "))
    carbon = eval(input("Carbon atoms: "))
    oxygen = eval(input("Oxygen atoms: "))
    weight = (hydrogen*1.0079) + (carbon*12.011) + (oxygen*15.9994)
    print("The molecular weight is", weight," grams/mole.\n")

import math
    
def q04():
    print("This is question 4 of lab03"); #Area of a triangle
    a = eval(input("Enter the length of the first side of the triangle:"))
    b = eval(input("Enter the length of the second side of the triangle:"))
    c = eval(input("Enter the length of the third side of the triangle:"))
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is ", area," square units.\n")
    
def q05():
    print("This is question 5 of lab03"); #Value of Gregorian epact
    year = eval(input("Enter the year (e.g.2012): "))
    C = (year)//100
    epact = (8+(C//4)-C+(((8*C)+13)//25)+11*((year)%19))%30
    print("The epact value is", epact,"days.\n")

q01()
q02()
q03()
q04()
q05()