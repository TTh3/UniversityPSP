import math
#
# File: welcome.py
# Author: your name
# Email Id: your email id
# Version: 1.0 5 August 2014
# Description: Practical 1 - displays a welcome message to the screen.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
# Display welcome message to the screen

def add(*num):
    totalValue=0
    for val in num:
        totalValue+=val
    print(totalValue)

def subtract(*num):
    totalValue=0
    for val in num:
        totalValue-=val
    print(totalValue)

def multiply(*num):
    totalValue=1
    for val in num:
        totalValue*=val
    print(totalValue)

def division(*num):
    totalValue=num[0]
    for val in num:
        totalValue/=val
    print(totalValue)

def squareArea(edge):
    print(edge **2)

def circleArea(radius):
    print(math.pi*radius**2)

add(1,10,5)
subtract(1,3,5)
multiply(1,3,5)
division(1,3,5)
squareArea(5)
circleArea(5)


# print('I\'m having fun and can\'t wait to learn more!')
# print("I'm having fun and can't wait to learn more!")
# print('I'm having fun and can't wait to learn more!')

print("I'm having fun and can't wait to learn more!")
print("I'm having fun and can't wait to learn more!")
print("I'm having fun and can't wait to learn more!") 

