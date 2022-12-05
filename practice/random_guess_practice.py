import random

number_to_be_guessed = random.randint(1, 10)

number_of_guesses = 1
while number_of_guesses < 2:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number_to_be_guessed:
        print("You guessed correctly")
        number_to_be_guessed += 1
