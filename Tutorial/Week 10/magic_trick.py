#
#  PSP - Week 10 Problem Solving Workout
#

number_set1 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59, 62, 63]
number_set2 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63]
number_set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61, 62, 63]
number_set4 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
number_set5 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]
number_set6 = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]



magic_number = 0

print('I can read your mind... think of a number between 1 to 63 (inclusive)')
print('Don\'t tell me... just be sure to keep it in your mind... I\'ll work it out')
print('by having you answer a few, simple questions....  :)')


# Your code solution goes here...   : )


def guess_number(card_list):
    total = 0
    for card in card_list:
        for cardindex in range(4):
            print(card[(8*cardindex):8*(cardindex+1)])
        cardInput = input("Is your numer in this pile y|n: ")
        if cardInput == 'y':
            total=total+card[0]
    return total

total = guess_number([number_set1,number_set2,number_set3,number_set4,number_set5,number_set6])












# Display the secret number to the screen and amaze your friends!  ; )
print('The number you are thinking about is.....', total)
