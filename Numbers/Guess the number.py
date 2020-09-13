import random
secretNumber = random.randint(1, 20)
print('I am thinking of a umber between 1 and 20.')

for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('The guess is to low.')
    elif guess > secretNumber:
        print('The guess is to high.')
    else:
        break;

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber));

