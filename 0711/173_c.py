h, w, k = map(int, input().split())
c = []
for i in range(h):
    li = input()
    c.append(li)

ans = 0
for ih in range(1 << h):
    for jw in range(1 << w):
        count = 0
        for i in range(h):
            for j in range(w):
                if (ih >> i & 1) == 0 and (jw >> j & 1) == 0:
                    if (c[i][j] == '#'):
                        count += 1
        if count == k:
            ans += 1
print(ans)
