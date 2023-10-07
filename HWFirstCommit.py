import math
import string
import re

#///////////////////// IF \\\\\\\\\\\\\\\\\\\\\\\#
#if(1)
def IfOne ():
    inputuser1 = int(input())
    inputuser2 = int(input())
    inputuser3 = int(input())

    print (inputuser1 , inputuser2 , inputuser3)

    if inputuser1 > inputuser2 and inputuser1 > inputuser3 :
        print(inputuser1)
    if inputuser2 > inputuser1 and inputuser2 > inputuser3 :
        print(inputuser2)
    if inputuser3 > inputuser1 and inputuser3 > inputuser2 :
        print(inputuser3)

#if(2)
def IfTwo ():
    inputuser1 = int(input())
    inputuser2 = int(input())
    inputuser3 = int(input())
    big = 0
    small = 0
    midle = 0
    if inputuser1 > inputuser2 and inputuser2 > inputuser3 :
        big = inputuser1 
        midle = inputuser2
        small = inputuser3
    elif inputuser2 > inputuser1 and inputuser1 > inputuser3 :
        big = inputuser2 
        midle = inputuser1
        small = inputuser3
    elif inputuser3 > inputuser1 and inputuser1 > inputuser2 :
        big = inputuser3 
        midle = inputuser1
        small = inputuser2
    elif inputuser3 > inputuser2 and inputuser2 > inputuser1 :
        big = inputuser3 
        midle = inputuser2
        small = inputuser1
    elif inputuser2 > inputuser1 and inputuser1 > inputuser3 :
        big = inputuser2 
        midle = inputuser1
        small = inputuser3
    elif inputuser2 > inputuser3 and inputuser3 > inputuser1 :
        big = inputuser2 
        midle = inputuser3
        small = inputuser1
    print(big,midle,small)

#if(3)
def IfThree ():
    userNumber = int(input("enter a Number (1_30):>"))
    if userNumber >= 1 and userNumber <= 7:
        print("1")
    elif userNumber >= 8 and userNumber <= 14:
        print("2")
    elif userNumber >= 15 and userNumber <= 21:
        print("3")
    elif userNumber >= 22 and userNumber <= 28:
        print("4")
    elif userNumber >= 29 and userNumber <= 30:
        print("5")

#4 
def IfFour ():
    userNumber = input('please enter a Number of Bynary Numbers (4bit) :)')
    
    if userNumber == '0001' or userNumber == '0010' or userNumber == '0100' or userNumber == '1000':
        print("1")
    elif userNumber == '0011' or userNumber == '0101' or userNumber == '0110' or userNumber == '1001' or userNumber == '1010' or userNumber == '1100':
        print("11")
    elif userNumber == '0111' or userNumber == '1011' or userNumber == '1101' or userNumber == '1110':
        print("111")
    elif userNumber == '1111':
        print("1111")

#if(5)
def IfFive ():
    userNumber1 = int(input('please enter a Number of Bynary Numbers (3bit) :)'))
    userNumber2 = int(input('please enter a Number of Bynary Numbers (3bit) :)'))
    One1 = userNumber1 % 10
    One2 = userNumber2 % 10
    Ten1 = math.floor(userNumber1 /10 % 10)
    Ten2 = math.floor(userNumber2 /10 % 10)
    Hundred1 = math.floor(userNumber1 / 100)
    Hundred2 = math.floor(userNumber2 / 100)
    One3 = One1 + One2
    Tan3 = Ten1 + Ten2
    Hundred3 = Hundred1 + Hundred2
    hezar = 0 
    if One3 >= 2:
        One3 -= 2
        Tan3 += 1
    if Tan3 >= 2:
        Tan3 -= 2
        Hundred3 += 1
    if Hundred3 >= 2 :
        Hundred3 -= 2
        hezar = 1
    if hezar == 1:
        print(str(hezar) + str(Hundred3) + str(Tan3) + str(One3) )
    else:
        print( str(Hundred3) + str(Tan3) + str(One3) )

#///////////////////// Loop \\\\\\\\\\\\\\\\\\\\\\\#

#Loop(1)
def LoopOne ():
    for i in range(100):
        userNumber = int(input())
        num2 = 1
        num1 = 0
        s = 0
        if userNumber % 2 == 1 :
            for j in range(25):
                num2 = num1 + num2
                num1 = num2 - num1
                if userNumber == num2 :
                    s += 1   
    print(s)

#Loop(2)
def LoopTwo ():
    userNumber = int(input())
    num1 = 0
    num2 = 1
    s = 0 
    for j in range(15):
        num2 = num1 + num2
        num1 = num2 - num1
        if userNumber % num2 == 0:
            s += 1
    print(s)

#Loop(3)
def LoopThree ():
    s = 0
    userNumber = input()

    for i in userNumber:
        if i == "0" :
            s += 1   
    print(s)

#Loop(4)
def Loopfour():
    string = ""
    userNumber = input()

    for i in userNumber:
        if i != "0" :
            string = string + i    
    print(string)

#Loop(5)
def LoopFive():
    for i in range (56,1984):
        for j in range(1,i):
            if i % j == 0 and j != 1 :
                print(j)

#///////////////////// array \\\\\\\\\\\\\\\\\\\\\\\#

#array(1)
def ArrayOne ():
    userNNumber = int(input())
    myArray = []

    for i in range(userNNumber):
        userNumber = input()
        myArray.append(int(userNumber))
        myArray.sort()
    print(myArray[len(myArray)-1])

#array(2)
def ArrayTwo ():
    userNNumber = int(input())
    myArray = []

    for i in range(userNNumber):
        userNumber = input()
        myArray.append(int(userNumber))
        myArray.sort()
        myArray.reverse()
    for j in myArray:
        print(j)

#array(3)
def ArrayThree ():
    userNNumber = int(input())
    myArray = []

    for i in range(userNNumber):
        userNumber = input()
        myArray.append(int(userNumber))
        myArray.sort()
    for j in myArray:
        print (myArray)
    print("yes")

#array(4)
def ArrayThree ():
    myArray = []
    myResult = set()
    for i in range (10):
        userName = int(input())
        myArray.append(userName)
    for j in (myArray):
        # print(j)
        for d in range(1,j):
            if(j % d == 0 and d != 1):
                a = j
                myResult.add(a)
    for i in (myResult):
        print(i)            
                
#array(5)
def ArrayFive ():
    userNumber = int(input())
    myArrayNum = []
    myArrayFact = []
    s = 1
    for i in range(userNumber):
        userNum = int(input())
        myArrayNum.append(userNum)
    for j in (myArrayNum):
        for d in range (1,j+1):
            s *= d
        myArrayFact.append(s)
        s=1
    for b in range (len(myArrayNum)):
        print(str(myArrayNum[b]) + ':' + str(myArrayFact[b]))         

#///////////////////// function \\\\\\\\\\\\\\\\\\\\\\\#

#Function(1)
def ArrayOne ():
    myArray = []
    for i in range(5):
        inputuser = int(input())
        myArray.append(inputuser)
    def EvenNumber (myArray):
        s = 0
        for j in (myArray):
            if j % 2 == 0:
                s += 1
        return s
    print(EvenNumber(myArray))

#Function(2)
def ArrayTwo ():
    myArray = []
    for i in range(5):
        inputuser = int(input())
        myArray.append(inputuser)
    def AveNumber (myArray):
        s = 0
        for j in (myArray):
            s += j
        s /= 5
        for d in (myArray):
            print(s)
            if d > s+3 or d < s-3:
                print(d)
    AveNumber (myArray)

#Function(3)
def ArrayThree ():
    inputNum = int(input())
    myArray = []
    for i in range(inputNum):
        inputUser = int(input())
        myArray.append(inputUser)
    def avalNumber (myArray):
        s = 0
        for i in (myArray):
            for j in range(1,i):
                if(i % j == 0 and j != 1): 
                    ali = 0 
                else:    
                    s += 1
        return s
    print(avalNumber(myArray))

#Function(4)
def ArrayFour ():
    inputNum = int(input())
    myArray = []
    myFact = []
    for i in range(inputNum):
        inputUser = int(input())
        myArray.append(inputUser)
    def avalNumber (myArray):
        s = 1
        for j in (myArray):
            for d in range (1,j+1):
               s *= d
            myFact.append(s)
            s = 1
        return myFact    
    print(avalNumber (myArray))

#Function(5)
def ArrayFive ():
    inputNum = int(input())
    myArray = []
    for i in range(inputNum):
        inputUser = int(input())
        myArray.append(inputUser)
    def maxTheMin (myArray):
        myArray.sort()
        myArray.reverse()
        print(myArray)
        return myArray
    maxTheMin (myArray)

#///////////////////// String \\\\\\\\\\\\\\\\\\\\\\\#

#string(1)
def StringOne ():
    ustring = input()
    string = string.capitalize()
    print(string)

#string(3)
def StringThree ():
    userInput = input()
    userInput.replace(a, '')

#string(4)
def Stringfour ():
    userInput = input()
    userInput.replace(' ', '')

#string(5)
def Stringfour ():
    userInput1 = input()
    userInput2 = input()
    Number = int(userInput1) + int(userInput2)
    print (str(Numbeer))
