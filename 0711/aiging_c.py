n = int(input())
ans = [0] * n
count = 0
for i in range(n):
    x = i + 1
    xx = x * x
    if  x * x >= n:
        break
    for j in range(n):
        y = j + 1
        yy = y * y
        if xx + yy + x * y>= n:
            break
        for k in range(n):
            z = k + 1
            zz = z * z
            kotae = xx + yy + zz + x * y + y * z + z * x
            if kotae > n:
                break
            ans[kotae-1] += 1
for i in range(n):
    print(ans[i])

