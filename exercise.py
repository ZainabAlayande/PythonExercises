number = int(input("Enter a number between 2 and 20: "))

while 2 <= number <= 20:
    if number % 2 == 0 and number % 3 == 0:
        print(number, "is between 2 and 20 and", number, "is divisible by 3")
        break

    else:
        print(number, "is between 2 and 20 and not divisible by 3")
        break


