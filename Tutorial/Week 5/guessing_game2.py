import random
number = random.randint(1, 10)
def get_guess():
    
    print('Random number is:', number)

    guess = int(input('Please enter your guess: '))
    print('You guessed:', guess)

    while guess < 1 or guess > 10:
        print('Number between 1 - 10')
    
        guess = int(input('Please enter your guess: '))
        print('You guessed:', guess)
    return guess
guess = get_guess()
while number != guess:

    if guess < number:
        print('Too low')
    elif guess > number:
        print('Too high')

    guess = int(input('Please enter your guess: '))
    print('You guessed:', guess)

    while guess < 1 or guess > 10:
        print('Number between 1 - 10')
        
        guess = int(input('Please enter your guess: '))
        print('You guessed:', guess)

print('Well done - you guessed it!')