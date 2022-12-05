#while the number does not equal one
#• If the number is odd, multiply by 3 and add 1
#• If the number is even, divide by 2
#• Use the new number and reapply the algorithm

number = int(input("Enter number: "))

while number == 1:
    if number % 2 != 0:
        number = (number * 3) + 1
        print("number is not even")
    else:
        number = number/2
        print("number is even")