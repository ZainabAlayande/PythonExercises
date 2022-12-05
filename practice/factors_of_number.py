number = int(input("Enter a number to get the factor: "))

counter = 1
factors_counter = 0

while counter <= number:
    if number % counter == 0:
        factors_counter = factors_counter + 1

    counter = counter + 1

print(number, "has", factors_counter, "factors")
