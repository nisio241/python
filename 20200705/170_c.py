x, n = map(int, input().split())
if n > 0:
    p = [int(i) for i in input().split()]
else:
    p = [0]

y = []
for i in range(102):
    if i not in p:
        y.append(i)

m = 102
ans = -1
for i in y:
    if abs(x-i) < m:
        m = abs(x-i)
        ans = i

print(ans)

