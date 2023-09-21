def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parents[y] = x


N = int(input())
parents = [i for i in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
for p in range(N):
    for q in range(p+1, N):
        if arr[p][q] == 0:
            continue
        print(find(p), find(q))
        if find(p) == find(q):
            print('WARNING')
            exit()
        union(p, q)
print('STABLE')
