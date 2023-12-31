"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""
V, E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
edge.sort(key=lambda x: x[2])
parents = [i for i in range(V)]


def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


cnt = 0
sum_weight = 0
for f, t, w in edge:
    if find_set(f) != find_set(t):
        union(f, t)
        cnt += 1
        sum_weight += w
        if cnt == V:
            break
print(sum_weight)
print(parents)
