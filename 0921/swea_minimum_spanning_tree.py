def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(V)]
    total = 0
    cnt = 0
    for k in range(E):
        if cnt == V:
            break
        s, e, w = edges[k]
        if find(s) == find(e):
            continue
        union(s, e)
        total += w
    print(f'#{tc}', total)
