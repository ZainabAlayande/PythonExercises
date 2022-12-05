counter = 1
largest = smallest = 0
while counter <= 5:
    number = int(input("Give me a number: "))
    if counter == 1:
        largest = smallest = number
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

    counter += 1
print("The largest number is", largest)
print("The smallest number is", smallest)
