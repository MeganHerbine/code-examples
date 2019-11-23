#Megan Herbine CSCI-181-01

def q01():
    print("This is question 1 of lab07"); #Easter calculator
    print("Easter Calculator for 1982-2018")
    year = eval(input("Enter the year: "))
    if 1982 <= year<= 2048:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19*a +24) % 30
        e = (2*b + 4*c + 6*d + 5) % 7
        
        day = 22 + d + e
        if day > 31:
            print("Easter is on April", day - 31,"\n")
        else:
            print("Easter is on March", day,"\n")
    else:
        print("That's not a year between 1982 and 2048.\n")
        
if __name__ == '__q01__':
    q01()    
    
def q02():
    print("This is question 2 of lab07"); #Leap year calculator
    
    def isLeap(year):
        if year % 4 != 0:
            return False
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
        
    def q2main():
        print("This program calculates whether a year is a leap year.")
        
        year = eval(input("Enter a year: "))
        if isLeap(year):
            print(year , "is a leap year.\n")
        else:
            print(year , "is not a leap year.\n")
            
    if __name__ == '__q2main__':
        q2main()
    
    q2main()

import isLeap
from isLeap import *

def q03():
    print("This is question 3 of lab07"); #Date validator
    print("Date Validator")
    DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def isValidDate(month, day, year):
        if 1 <= month <= 12:
            if month == 2:
                if isLeap(year):
                    lastDay = 29
                else :
                    lastDay = 28
            else:
                lastDay = DAYS_IN_MONTH[month]
            if 1 <= day <= lastDay:
                return True
        return False

    def q3main():
        month, day, year = input("Enter a date (mm/dd/yyyy): ").split("/")
        if isValidDate(int(month), int(day), int(year)):
            print("The date is valid.\n")
        else:
            print("The date is invalid.\n")
    if __name__ == '__q3main__':
        q3main()
        
    q3main()
    
import isLeap
from isLeap import *
import isValidDate
from isValidDate import *

def q04():
    print("This is question 4 of lab07"); #Day number calculation
    
    def dayNumber(month, day, year):
        dayNum = 31*(month - 1) + day
        
        if month > 2:
            dayNum = dayNum - (4*month + 23)//10
            
        if isLeap(year):
            if month > 2:
                dayNum = dayNum + 1
                
        return dayNum
    
    def q4main():
        print("Day Number Calculation: ")
        
        month, day, year = input("Enter date (mm/dd/yyyy): ").split("/")
        day, month, year = int(day), int(month), int(year)
        
        if isValidDate(month, day, year):
            print("The day number is", dayNumber(month, day, year),"\n")
        else:
            print("That's an invalid date!\n")
            
    if __name__ == "__q4main__":
        q4main()
        
    q4main()
   
def q05():
    print("This is question 5 of lab07"); #I love exception
    
    class IloveError(Exception):
        def __init__(self, value):
            self.value=value
            
        def __str__(self):
            return (repr(self.value))  
    
    try:
            raise(IloveError(3*2))
        
    except IloveError as error:
        print("I love exception has occured~!!", error.value,"\n")   

import math
from graphics import *
    
def q06():
    print("This is question 6 of lab07"); #Archery scorer
    
    def targetWindow():
        win = GraphWin("Archery Scorer", 400, 400)
        win.setCoords(-6, -6, 6, 6)
        win.setBackground("gray")
        center = Point(0,0)
        
        c1 = Circle(center, 5)
        c1.setFill("white")
        c1.draw(win)
        c2 = Circle(center, 4)
        c2.setFill("black")
        c2.draw(win)
        c3 = Circle(center, 3)
        c3.setFill("blue")
        c3.draw(win)
        c4 = Circle(center, 2)
        c4.setFill("red")
        c4.draw(win)
        c5 = Circle(center, 1)
        c5.setFill("yellow")
        c5.draw(win)
        
        return win
    
    def drawInterface(win):
        msg = Text(Point(0, 5.5), "Click where arrow lands")
        msg.setStyle("bold")
        msg.setSize(14)
        msg.draw(win)
        
        arrowBox = Text(Point(-4, -5.5), "Arrow: ")
        arrowBox.setStyle("bold")
        arrowBox.draw(win)
        
        totalBox = Text(Point(4, -5.5), "Total: ")
        totalBox.setStyle("bold")
        totalBox.draw(win)
        
        return msg, arrowBox, totalBox
    
    def getScore(pt):
        x,y = pt.getX(), pt.getY()
        dist = math.sqrt(x*x + y*y)
        if dist <= 1:
            score = 9
        elif dist <= 2:
            score = 7
        elif dist <= 3:
            score = 5
        elif dist <= 4:
            score = 3
        elif dist <= 5:
            score = 1
        else:
            score = 0
        return score
    
    def mainq6():
        win = targetWindow()
        msg, arrowBox, totalBox = drawInterface(win)
        
        arrow = 0
        total = 0
        for i in range(5):
            hit = win.getMouse()
            dot = Circle(hit, 0.1)
            dot.setFill("green")
            dot.draw(win)
            score = getScore(hit)
            arrowBox.setText("Arrow: {0:1}".format(score))
            total = total + score
            totalBox.setText("Total: {0:2}".format(total))
            
        msg.setText("Click anywhere to quit.")
        win.getMouse()
        win.close()
    
    mainq6()        

q01()    
q02()
q03()
q04()
q05()
q06()