#Created: Feb 25, 2019
#Lastest implement: Apr. 22, 2019

import math
print("-------------------------------")
print("----- Triangle Calculator -----")
print("-------------------------------")
print("")
#==================================== Function

def checkTriangle(a,b,c):
    print("Calculating . . . .")
    lists = [a,b,c]
    lists.sort()
    lists2 = [lists[0]**2, lists[1]**2, lists[2]**2]
    print("Result:",end=" ")
    if lists[2] > lists[0] + lists[1]:
        print("-> Not a triangle")
    elif lists2[2] == lists2[0] + lists2[1]:
        print("-> Right Triangle")
    elif a == b == c:
        print("-> Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("-> Isosceles Triangle")
    else:
        print("-> Scalene Triangle")

def sideCgeneration(a, b, mode):
    list = [a,b]
    list.sort()
    if mode == 1:
        c = math.sqrt(list[0]**2 + list[1]**2)
        sideC = float(format(c, '.2f'))
        print("Result: Side C is " + str(sideC))
    elif mode == 2:
        if a == b:
            sideC = float(format(a, '.2f'))
            print("Result: Side C is " + str(sideC))
        else:
            print("* Side A and B not equal")
    elif mode == 3:
        if a == b:
            sideC = a + b - 1
            print("Result: Side C is " + str(sideC))
        else:
            sideC = float(format(list[1], '.2f'))
            print("Result: Side C is " + str(sideC))
    elif mode == 4:
        sideC = a + b - 1
        print("Result: Side C is " + str(sideC))
    else:
        print("* Something went wrong")

#==================================== Main Program 
   
inputCheck = True
while(inputCheck):
    try:
        print("")
        selectMode = str(input("Select Mode: 1. Normal Triangle Calculator 2. Enchance Calculator (1 or 2): "))
        if (selectMode == '1'):
            sideA = float(input("Enter Side A: "))
            sideB = float(input("Enter Side B: "))
            sideC = float(input("Enter Side C: "))

            sideA = float(format(sideA, '.2f'))
            sideB = float(format(sideB, '.2f'))
            sideC = float(format(sideC, '.2f'))

            if sideA <= 0 or sideB <= 0 or sideC <= 0:
                print("Your input are invalid. Please enter side again")

            elif sideA >= 1000 or sideB >= 1000 or sideC >= 1000:
                inputCheck = True
                print("Your input are invalid. Please enter side again")
            else:
                inputCheck = False
                checkTriangle(sideA, sideB, sideC)

        elif (selectMode == '2'):
            sideA = float(input("Enter Side A: "))
            sideB = float(input("Enter Side B: "))
            print("Select your triangle for generates side C:")
            print(" 1. Right Triangle")
            print(" 2. Equilateral Triangle")
            print(" 3. Isosceles Triangle")
            print(" 4. Scalene Triangle")
            mode = int(input("Select your mode: "))
            print()
            sideCgeneration(sideA, sideB, mode)
            inputCheck = False

    except:
        print("Your input are invalid. Please enter side again")
    print("")

input("----- End of the program -----")