number = int(input("Enter a number, enter any negative number to stop: "))

counter = 0
sumOfEvenNumbers = 0
sumOfOddNumbers = 0
numberOfEvenNumbers = 0
numberOfOddNumbers = 0

while number > -1:

    if number % 2 == 0:
        sumOfEvenNumbers = sumOfEvenNumbers + number

    if number % 2 == 0:
        numberOfEvenNumbers = numberOfEvenNumbers + 1

    if number % 2 != 0:
        sumOfOddNumbers = sumOfOddNumbers + number

    if number % 2 != 0:
        numberOfOddNumbers = numberOfOddNumbers + 1

        counter = counter + 1

    number = int(input("Enter a number, enter any negative number to stop: "))

print()
print("Number of Odd Number is: ", numberOfOddNumbers)
print("Number of Even Number is: ", numberOfEvenNumbers)
print()
print("Sum of Odd Number is: ", sumOfOddNumbers)
print("Sum of Even Number is: ", sumOfEvenNumbers)
