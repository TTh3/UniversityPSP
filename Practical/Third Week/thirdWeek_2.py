#
# File: thirdWeek_2.py
# Author: Jaylord
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Practical 3, Excercise 2
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# a)
k=1
while k<5:
    print("Stuck in a loop!")
    k+=1
else:
    print('okay then...')
'''
Stuck in a loop!
Stuck in a loop!
Stuck in a loop!
Stuck in a loop!
okay then...
'''

# b)
k=6
while k>=2:
    print('Still looping.')
    k=k-2
'''
Still looping.
Still looping.
Still looping.
# k=0
'''

# c)
num1=2
num2=4
if(num1<num2):
    print('Yes.')
'''
Yes.
'''

# d)
str1= "kramer"
str2 = "george"
if str1== str2:
    print("Equal.")
else:
    print("Not equal.")
'''
Not equal.
'''

# e)
mark = 78
if mark>=85:
    print('HD')
elif mark>=75:
    print('D')
elif mark>=65:
    print('C')
elif mark>=55:
    print('P1')
elif mark >=50:
    print('P0')
elif mark >=40:
    print('F1')
else:
    print('F2')
'''
D
'''