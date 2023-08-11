N = int(input())
C = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
for i in range(C):
    c1, c2 = map(int, input().split())
    arr[c1][c2] = 1
    arr[c2][c1] = 1
visited = [0] * (N+1)


def dfs(n):
    visited[n] = 1
    for i in range(N+1):
        if arr[n][i] == 1 and visited[i] == 0:
            dfs(i)


dfs(1)
print(visited.count(1) - 1)
