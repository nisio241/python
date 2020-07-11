import itertools
h, w, k = map(int, input().split())
c = [list(input()) for i in range(h)]
c_x = list(range(w))
c_y = list(range(h))

c_x_conb = []
for n in range(1,len(c_x)+1):
    for conb in itertools.combinations(c_x, n):
        c_x_conb.append(list(conb)) 

c_y_conb = []
for n in range(1,len(c_y)+1):
    for conb in itertools.combinations(c_y, n):
        c_y_conb.append(list(conb)) 

ans = 0
for i in c_y_conb:
    c_dump = c.copy
    count = 0
    for j in i:
        for k in range(w):
            c_dump[j][k] = '.'
    for l in range(h):
        count = c_dump[l].count('#')
    if count == k:
        ans += 1


for i in c_x_conb:
    c_dump_2 = c.copy
    count = 0
    print(i)
    for j in i:
        for k in range(h):
            c_dump[k][j] = '.'
    print(c_dump_2)
    for l in range(h):
        count = c_dump_2[l].count('#')
    if count == k:
        ans += 1
print(ans)
