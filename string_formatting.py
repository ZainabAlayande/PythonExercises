name = "Aliyah"
age = 18.7658

s = "{0} is {1} years old, and {2} loves Java".format(name, age, "Java")
s = "{0:^20} is {1:>10.2f} years old, and {2} loves Java".format(name, age, "Java")
s = f"{name=:$^20} is {age:>10.2%} years old, and {name} loves {'Java'}"

print(s)

hello = "hello world"
for index, letter in enumerate(hello):
    print(f"{letter} -> {index}")

for index in range(len(hello)):
    print(f"{hello[index]} --> {index}")

for i in range(1, 21):
    s = "*" * i
    #print(f"{s:^20}")
    print(f"{s:20}{s:^20}{s:>20}")