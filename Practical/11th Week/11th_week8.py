#
# File: 11th_week8.py
# Author: Jaylord Silverio
# Email Id: siljd001@mymail.unisa.edu.au
# Description: Week 11 - Practical (File Input and Output)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

SeventhExMod = __import__("11th_week7")


PASSWORD_LENGTH = 8
password_count = int(input("Number of Generated Passwords: "))
password = []
for _ in range(password_count):
    password.append(SeventhExMod.generate_password(PASSWORD_LENGTH))
    
print(password)


    


