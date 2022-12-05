counter = 0


while counter < 100:
   print(counter)
   counter = counter + 1

counter = 1

while counter <= 100:

    if counter % 15 == 0:
        print("fizzbuzz")

    elif counter % 3 == 0:
        print("fizz")

    elif counter % 5 == 0:
        print("buzz")

    else:

        print(counter)
    counter = counter + 1

# word = "Hello world!"

# for letter in word:
#    print(letter)

#number = int(input("Enter a number: "))

#factor = 1
#sum_of_factors = 0

#while factor < number:
#    if number % factor == 0:
#        sum_of_factors = sum_of_factors + factor

#    factor = factor + 1

#if sum_of_factors < number:
#    print(number, "is deficient")

#elif sum_of_factors > number:
#    print(number, "is abundant")

#else:
#    print(number, "is a perfect number")

#print(factor)
#print(sum_of_factors)


