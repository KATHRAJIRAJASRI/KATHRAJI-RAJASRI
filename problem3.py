a = int(input("Enter a number: "))
if a % 2 == 0:
    count = a - 1
else:
    count = a
i = 0
num = 1
while i < count:
    print(num, end="")

    if i < count - 1:
        print(", ", end="")

    num = num + 2
    i = i + 1
