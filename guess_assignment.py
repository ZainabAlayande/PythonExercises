import random

#number_to_be_guessed = random.randint(1, 100)
number_to_be_guessed = 78

number_of_guess_time = 1

guess = int(input("Guess a number between 1 and 100: "))

while number_of_guess_time <= 2:

    if guess > number_to_be_guessed:
        print("Number is too high")

    elif guess < number_to_be_guessed:
        print("Number is too low")

    else:
        print("You got it right")
        break

    guess = int(input("Guess a number between 1 and 100: "))



    print("Try again later, It's unfortunate you could not guess", number_to_be_guessed)