import random

print("This is a number guessing game.\nYou have 7 chances to guess the correct number (1-100).\nLet's begin!")

number_to_guess = random.randint(1, 100)
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please enter your guess : "))
    if my_guess == number_to_guess:
        print("Correct! ", number_to_guess, " is the required number.")
        break
    elif guess_counter == chances and my_guess != number_to_guess:
        print("You have run out of chances.")
        print("The correct number is ", number_to_guess, ".")
    elif my_guess > number_to_guess:
        print("Your guess is higher.")
    elif my_guess < number_to_guess:
        print("Your guess is lower.")