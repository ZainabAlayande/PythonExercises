number = float(input("Enter an integer, the input ends on 0: "))

total = 0
counter = 0
count_of_positive_number = 0
count_of_negative_number = 0

while number != 0:

    if number > 0:
        count_of_positive_number = count_of_positive_number + 1
        total = total + number

    if number < 0:
        count_of_negative_number = count_of_negative_number + 1
        total = total + number

    number = float(input("Enter an integer, the input ends on 0: "))
    counter = counter + 1

print()
print("The count of positive number is ", count_of_positive_number)
print("The count of negative number is ", count_of_negative_number)
print("The total is ", total)
print("The average is ", total / counter)

