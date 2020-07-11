n, m = map(int, input().split())
h = [int(i) for i in input().split()]
road = [list(map(int, input().split())) for i in range(m)]
y = []
for i in range(m):
    for j in range(2):
        if road[i][j] == 1:
            y.append(road.pop(i))
            break;

print(y)

