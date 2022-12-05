hello = "hello There!!!"

print(hello.endswith("!!!"))
print(hello.startswith("h"))

print(hello.isupper())
print(hello.isalpha())

print(hello.isdecimal())
print(hello.islower())

print()

print(hello.replace("l", "q"))
print(hello.replace("l", "q", 1))
print(hello.replace("l", "q", 2))

print()

print(hello.lstrip())

print()

print(hello.zfill(20))
a, b = hello.split()
print(hello.split())
print(hello.split("e"))

print()

print(hello.partition("e"))
print(hello.rpartition("e"))

print()

print(" -- ".join(["a", "b", "c"]))
print()

bin_ = "10110101101011078"
print(bin_.replace("1", "X"). replace("0", "1"). replace("X", "0"))
print(bin_.translate(str.maketrans("01", "10")))
print(bin_.translate(str.maketrans("01", "10", "8")))
