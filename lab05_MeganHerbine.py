#Megan Herbine CSCI-181-01

def q01():
    print("This is question 1 of lab05"); #number value of name
    names = input("Enter a name: ")
    letters = "".join(names.split(' '))
    letters = letters.lower()
    
    sum = 0
    for letter in letters:
        sum = sum + (ord(letter) - ord('a') + 1)
        
    print("The value is: ", sum,"\n")
     
def q02():
    print("This is question 2 of lab05"); #caeser cipher
    key= eval(input("Enter the key value: "))
    plain = input("Enter the phrase to encode: ")
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    
    cipher = ""
    for letter in plain:
        pos = chars.find(letter)
        newpos = (pos + key)%53
        cipher = cipher + chars[newpos]
        
    print("Encoded message follows:")
    print("", cipher,"\n")

def q03():
    print("This is question 3 of lab05"); #chaotic function    
    x1 = eval(input("Enter the first seed between 0 and 1: "))
    x2 = eval(input("Enter the second seed between 0 and 1: "))
    
    print()
    print("index     ", x1, "        ", x2)
    print("--------------------------------")
    
    for i in range(1, 11):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("{0:^5} {1:^15.6f} {2:^10.6f}".format(i, x1, x2),"\n")
    
def q04():
    print("This is question 4 of lab05"); #future value
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))
    
    print()
    print("Year    Value")
    print("---------------")
    
    for i in range(years+1):
        print("{0}     ${1:0.2f}".format(i, principal))
        principal = principal * (1 + apr)
    
q01()
q02()
q03()
q04()