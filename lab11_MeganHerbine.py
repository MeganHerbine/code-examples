#Megan Herbine CSCI-181-01

from math import sqrt

def q01():
    
    def getNumbers():
        nums=[]
        
        xStr = input("Enter a number (<Enter> to quit) >> ")
        while xStr != "":
            x = eval(xStr)
            nums.append(x)
            xStr = input("Enter a number (<Enter> to quit) >> ")
        return nums
    
    def mean(nums):
        sum = 0.0
        for num in nums:
            sum = sum + num
        return sum / len(nums)
    
    def stdDev(nums, xbar):
        sumDevSq = 0.0
        for num in nums:
            dev = num - xbar
            sumDevSq = sumDevSq + dev * dev
        return sqrt(sumDevSq/(len(nums)-1))
    
    def median(nums):
        nums.sort()
        size = len(nums)
        midPos = size // 2
        if size % 2 == 0:
            median = (nums[midPos] + nums[midPos-1]) / 2.0
        else:
            median = nums[midPos]
        return median
    
    def q01main():
        print("This is question 1 of lab11")
        print("This program computes mean, median, and standard deviation.")
        data = getNumbers()
        xbar = mean(data)
        std = stdDev(data, xbar)
        med = median(data)
        
        print("The mean is", xbar)
        print("The standard deviation is", std)
        print("The median is", med,"\n")
        
    if __name__ == '__q01main__':
        q01main()
        
    q01main()
    
def q02():
    print("This is question 2 of lab 11")
    
    def count(myList, x):
        sum = 0
        for i in range(len(myList)):
            if myList[i] == x:
                sum = sum + 1
            else:
                sum = sum + 0
        return sum

    lst = eval(input("Enter a list in the form [1, 2, 3]: "))
    y = eval(input("Enter the number that you want to count the occurrences of: "))

    print(count(lst, y))

    def isin(myList, x):
        if count(myList, x) > 0:
            return True
        else:
            return False
    
    lst = eval(input("Enter a list in the form [1, 2, 3]: "))
    y = eval(input("Enter a number to check if it's in the list: "))
    
    print(isin(lst, y))

    def index(myList, x):
        for i in range(len(myList)):
            if myList[i] == x:
                ind = i
        return ind 
    
    lst = eval(input("Enter a list in the form [1, 2, 3]: "))
    y = eval(input("Enter a number to find its index: "))
    
    print(index(lst, y))
    
    def reverse(myList):
        newList=[]

        for item in myList:
            newList.insert(0, item)
        return newList
    
    lst = eval(input("Enter a list in the form [1, 2, 3]: "))

    print(reverse(lst),"\n")
    
from random import randrange

def q03():
    
    print("This is question 3 of lab11")
    
    myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

    def shuffle(myList):
        newList = []
        for i in range(len(myList)):
            itemMove = randrange(0, len(myList))
            newList.append(myList[itemMove])
            myList.pop(itemMove)
        return newList
    
    print("This is in original order.")
    print(myList)
    print("This should be in random order.")
    print(shuffle(myList),"\n")

def q04():    
    
    def innerProd(x,y):
        sum = 0
        for i in range(len(x)):
            sum = sum + x[i] * y[i]
        return sum

    print("This is question 4 of lab 11")
    lst1 = eval(input("Enter first list (in the form [1,2,3]): "))
    lst2 = eval(input("Enter second list (in the form [4,5,6]): "))

    print("The inner product is", innerProd(lst1,lst2),"\n")

def q05():
    
    def removeDuplicates1(lst):
        lst2 = []
        for item in lst:
            if item not in lst2:
                lst2.append(item)
        lst.clear()        
        lst.extend(lst2)
        
    def q05main():
        lst1 = [3, 5, 6, 8, 9, 9, 9, 3, 1, 2, 7, 10]
        lst2 = [10, 11, 12, 6, 12, 14, 13, 13, 9, 7, 10]
        
        print("This is question 5 of lab 11")
        print("Here are the two in original list with duplicated elements.")
        print(lst1)
        print(lst2)
        removeDuplicates1(lst1)
        print("This should have no duplicated members in list 1.")
        print(lst1)
        removeDuplicates1(lst2)
        print("This should have no duplicated members in list 2.")
        print(lst2)
        
    if __name__ == '__q05main__':
        q05main()
        
    q05main()
            
q01()
q02()
q03()
q04()
q05()