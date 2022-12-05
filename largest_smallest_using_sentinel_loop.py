number = int(input("Enter a number(Punch 0 to stop):"))

largest = smallest = number

while number != 0:

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    number = int(input("Enter a number(Punch 0 to stop):"))
print()
print("Largest is: ", largest)
print("Smallest is:", smallest)

































# counter = 0
#number = int(input("Enter a number, (punch -1 to stop): "))
#largest = number
#smallest = number

#while number != -1:
    # counter = counter + 1

    #    if number > largest:
    #        largest = number

    #if number < smallest:
    #   smallest = number

    #number = int(input("Enter a number, (punch -1 to stop): "))
    #if number == -1:
    #   print()

    #   print("Smallest Number is:", smallest)
#   print("Largest Number is:", largest)
