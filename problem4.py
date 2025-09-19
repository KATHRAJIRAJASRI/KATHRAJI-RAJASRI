numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
i = 1
while i <= 9:
    count = 0
    j = 0
    while j < 11:
        num = numbers[j]
        if num % i == 0:
            count = count + 1
        j = j + 1
    print(i, ":", count)
    i = i + 1
