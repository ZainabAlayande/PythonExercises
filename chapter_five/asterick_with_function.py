def function():
    number_of_rows = int(input("Enter number of rows "))
    for i in range(0, number_of_rows):
        for j in range(0, i + 1):
            print("*", end="")
        print()


function()