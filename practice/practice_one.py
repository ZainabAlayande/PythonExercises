count = 0

largest = float("-inf")
smallest = float("+inf")
second_largest = 0

while count < 5:
    num = int(input("Enter a number: "))

    if num > largest:
        second_largest = largest
        largest = num

    if num < smallest:
        smallest = num

    count += 1

print("Largest number", largest)
print("Smallest number", smallest)
print("Second Largest", second_largest)
