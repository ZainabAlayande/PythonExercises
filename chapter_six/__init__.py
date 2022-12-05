#user_input = int(input("Enter a number: "))

#if user_input == 30:
#    print("Start Class")

#elif user_input >= 20 | user_input <= 29:
#    print("Start class still")

#else:
#    print("Get Lost")

#value = "functions"
#for C14 in value:
#    print(C14)

#print(len(value))

value = "Hello blessing"
for i in value:
    print(i)
    if i != "b":
        print(i)

for i in range(len(value)):
    if value[i] == "b":
        print(i)
        if value[i] != "b":
            print(value[i], ":", i)

for index, value in enumerate(value):
    if value == "b":
        if value != "b":
            print(value)
        print(value, ":", index)
        print("Character b is:", index)

print(index)