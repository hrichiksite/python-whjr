import random

chances = 0
randomNumber = random.randint(0, 10)

while chances < 3:
    number = int(input("Guess a number between 0 and 10: "))
    if number == randomNumber:
        print("You guessed it!")
        break
    elif number < randomNumber:
        print("Too low!")
    else:
        print("Too high!")
    chances += 1

print('The number was', randomNumber)
print('You had', chances, 'chances')