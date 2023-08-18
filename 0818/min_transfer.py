N, M = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    m1, m2 = map(int, input().split())
    arr[m1][m2] = arr[m2][m1] = 1
T = int(input())

visited = [0] * (N+1)
queue = [1]
visited[1] = 1
while queue:
    t = queue.pop(0)
    for i in range(1, N+1):
        if i != T:
            if arr[t][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
if visited[N]:
    print(visited[N] - 1)
else:
    print(-1)
