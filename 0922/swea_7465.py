def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    cnt = 0
    for k in range(1, N+1):
        if k == parents[k]:
            cnt += 1
    print(f'#{tc}', cnt)