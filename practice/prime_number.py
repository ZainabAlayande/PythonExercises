number = int(input("Enter a number: "))

counter = 2
factors_counter = 0

while counter < number:
    if number % counter == 0:
        print(number, "is a prime number",)

    if number % counter != 0:
        factors_counter = factors_counter + 1

        print(number, "is not a prime number", )

    counter = counter + 1