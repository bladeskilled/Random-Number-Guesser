from multiprocessing.connection import wait
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Error, Please type a number larger than 0.')
        quit()
else:
    print('Error, please type a number.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
       user_guess = int(user_guess)
    else:
        print('Error, please type a number.')
        continue

    if user_guess == random_number:
        print("Your guess was correct.")
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")

print("You got the number correct in", guesses, "guesses.")