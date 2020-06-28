y = [1, 2, 3, 4, 5,]
for i in y:
    print(i)

for i in range(2):
    print(y[i])

x = [[1, 2, 3], [4, 5, 6]]
for i in x:
    print(i)

for rows in x:
    for columuns in rows:
        print(columuns)

for i in range(1):
    for j in range(2):
        print(x[i][j])
