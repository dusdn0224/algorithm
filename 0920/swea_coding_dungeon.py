N, M, K = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    m1, m2, C = map(int, input().split())
    arr[m1].append([m2, C])
q = [[0, 0]]
visited = [0] * N
while q:
    t, gold = q.pop(0)
    visited[t] = gold
    for i in arr[t]:
        q.append([i[0], gold + i[1]])
for d in range(1, N):
    if visited[d] <= K:
        print(d, end=' ')