# Second Week - Standard Libraries | Inputs | If Statements
import math
import random as rand
def StandardBuiltInFuncs():
    width=10
    height=5
    area = width *height
    print(area)
    areaAbsolute = abs(area)
    print(areaAbsolute)
    resultPow = pow(2,3)
    print(resultPow)
    print(round(5.3))
    print(int('7')+int('2'))
    print(float('1.5')+float(1))
    print([i for i in range(1,6)])
    print(str(2)+str(3))
    print('Wow',"! ", "The answer is: ", width, sep="")

def InputOutputFuncs():
    guess = input('Please enter your guess: ')
    name = input('Please enter your name: ')
    number= int(input('Enter Number: '))
    print("Your guess is:",guess,"\n", "Your name is:",name,"\n", "Your number is:", number)

def numeric_math_modules():
    # Math Modules
    print(math.ceil(23)+math.pi)
    # Random Modules
    NumList = [5,3,7,3]
    print(rand.random())
    print(rand.choice(NumList))
    print(rand.shuffle(NumList))



