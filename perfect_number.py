number = int(input("Enter a number: "))

counter = 1
factor = 0
sum_of_factor = 0

while counter < number:
    if number % counter == 0:
        sum_of_factor = sum_of_factor + number
    counter += 1

if sum_of_factor > number:
    print(number, "is an abundant number")

elif sum_of_factor < number:
    print(number, "is a deficient number")

if sum_of_factor == number:
    print(number, "is a perfect number")


print("Sum of factor is: ", sum_of_factor)
