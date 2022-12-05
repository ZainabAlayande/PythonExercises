number = int(input("Enter a number: "))

factors = 1
for i in range(number, 0, -1):
    factors = i * 1

    print(i, end="*")


