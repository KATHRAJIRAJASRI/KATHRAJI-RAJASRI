a = int(input("Enter a number: "))
i = 0
num = 1
while i < a:
    print(num, end="")
    if i < a - 1:
        print(", ", end="")
    num = num + 2
    i = i + 1
