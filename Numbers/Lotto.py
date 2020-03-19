'''A program which asks for 6 numbers in the range 1-49.
 The program should display 6 random numbers from the same range.
 Check how many numbers the user guessed. '''

import random
import sys

# Make a list for the winning numbers
winning_number = []
guessed_numbers = 0

# Geting 6 random numbers and add them to the winning list
for i in range(1, 7):
    winning_number.append(random.randint(1,49))
print(winning_number)
# Ask the player to input 6 numbers
while True:
    try:
        player_numbers = [int(number) for number in input("Give me 6 numbers between 1 and 49: ").split()]
        break
    except:
        print("Just numbers...")

# Check if the numbers are between 1 and 49
for y in range(0, 6):
     if player_numbers[y] >= 1 and player_numbers[y] <=49:
         continue
     else:
         sys.exit("Only numbers between 1 and 49.")

# Check if the player only enters 6 numbers
if len(player_numbers) == 6:

    # Finding out how many numbers the player guessed
    for i in range(0, 6):
        if player_numbers[i] == winning_number[i]:
            guessed_numbers += 1

    # Print different messages for every situation
    if guessed_numbers == 6:
        print("WOW! You just guessed all the numbers. Here, the jackpot is yours! :)")
    elif guessed_numbers == 5:
        print("Great job, you guessed " + str(guessed_numbers) + " numbers!")
    elif guessed_numbers == 4:
        print("Yeah, good. " + str(guessed_numbers) + " numbers guessed.")
    elif guessed_numbers == 3:
        print("You won 10 bucks for a meal. You guessed " + str(guessed_numbers) + " numbers.")
    else:
        print("Try again bro. You guessed " + str(guessed_numbers) + " numbers..." )

    # Print the winning numbers and the player numbers
    print("The winning numbers were: " + str(winning_number)[1:-1])
    print("Also, your picked numbers: " + str(player_numbers)[1:-1])

else:
    print("Give me 6 numbers, not " + str(len(player_numbers)))
