X = int(input())
Y = 100
count = 0
while Y < X:
    Y = Y + Y // 100
    count += 1

print(count)

