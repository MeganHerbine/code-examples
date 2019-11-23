#Megan Herbine CSCI-181-01
#Lab calculating temperature in Fahrenheit and Celsius, 
#average test score, time in hours, minutes, and seconds, 
#and value of a 10-year investment

def q01():
    print("This is question 1 of lab02"); #Celsius to Fahrenheit
    celsius = eval(input("What is the Celsius temperature?"))
    fahrenheit = (9/5) * celsius + 32
    print("The temperature is ",fahrenheit," degrees Fahrenheit.\n")
    
def q02():
    print("This is question 2 of lab02"); #Fahrenheit to Celsius
    fahrenheit = eval(input("What is the Fahrenheit temperature?"))
    celsius = (5/9) * (fahrenheit - 32)
    print("The temperature is ",celsius," degrees Celsius.\n")

def q03():
    print("This is question 3 of lab02"); #Average of 3 test scores
    first = eval(input("Enter the first test score:"))
    second = eval(input("Enter the second test score:"))
    third = eval(input("Enter the last test score:"))
    average = (first + second + third)/3
    print("The average score is ",average,"\n")

def q04():
    print("This is question 4 of lab02"); #Time in hours, minutes, and seconds
    total_seconds = float(input("Enter a number of seconds:"))
    hours = int((total_seconds/60)/60)
    minutes = int((total_seconds/60) % 60)
    seconds = int(total_seconds % 60)
    print("Here is the time in hours, minutes, and seconds:")
    print("Hours:", float(hours))
    print("Minutes:", float(minutes))
    print("Seconds:", float(seconds),"\n")
    
def q05():
    print("This is question 5 of lab02"); #Value of investment
    print("This program calculates the future value of a 10-year investment.");
    principal = eval(input("Enter the initial principal:"))
    apr = eval(input("Enter the annual interest rate:"))
    for i in range (10) :
        principal = principal * (1 + (apr))
    print("The value in 10 years is:", principal,"\n")        
    
q01()
q02()
q03()
q04()
q05()