# words = "I don't understand cohort 14"
# x = 0
# for words in range:
# if x == "understand":
# print("x")

#Print per character
#s = 'Simplilearn'
#for i in s:
#    print(i, end=" ")

#Use for loop in a list
#programming = ["Java", "Python", "Ruby", "HTML"]
#for iter in programming:
#    print(iter)

#find average of a list of numbers
#list_of_number = [20,25,10,50,45]
#sum = 0
#for i in list_of_number:
#    sum = sum + i
#   #average = sum/len(list_of_number)
#print("sum =", sum)
#print("Average", sum/len(list_of_number))

#For loop using a tuple
#num = (30, 45, 60, 50, 70)
#sum = 0
#for i in num:
#    sum = sum + i
#    print(sum)

#range function - to iterate over a range of values
#for i in range(1, 10):
#    print(i)

#for loop with an interval
#for i in range(1, 10, 2):
#    print(i)

#Program to print multiplication table of given number
#n = int(input("Enter a number: "))
#for i in range(1, 11):
#    mul = n * i
#    print(n, "*", i, "=", mul)

#list = ["Zainab", "Abdulmalik", "Ogechi", "Eniobanke", "Atinuke", "Aishat"]
#for i in range(len(list)):
#    print("Hello", list[i])


#list2 = ["Zainab", "Abdulmalik"]
#for i in range(len(list2)):
#    print("Hello", list2[i])

#for loop with else clause
#for i in range(0, 10, 3):
#    print(i)
#else:
#    print("The loop has completed execution")


#Break
#for i in range(1, 10):
#    if (i == 6):
#        break
#    print(i)


#Continue
#for i in range(1, 10):
#    if (i==6):
#        continue
#    print(i)

#Display total goals a player scored

#player_name = "Carmelo"
#goals ={"Edison": 14, "Carmelo": 7, "Kins": 10}
#for i in goals:

#for i in range(10, 0, -1):
#    print(i, end=" * ")

#    if i == player_name:
#        print(goals[i])
#        break
#else:
#    print("No player with that name found")

#Cube of number
#number = [2, 5, 7, 4, 8, 6]
#cube = []
#for i in number:
#    cube.append(i**3)
#   print(cube)


#Pattern Printing
number_of_rows = int(input("Enter number of rows "))
for i in range(0, number_of_rows):
    for j in range(0, i+1):
        print("*", end="")
    print()
