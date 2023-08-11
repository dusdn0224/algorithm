N, K = map(int, input().split())
S = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    k1, k2 = map(int, input().split())
    arr[k1][k2] = 1


def dfs_pre(s):
    global visited
    visited[s] = 1
    print(s, end=' ')
    for i in range(N, 0, -1):
        if arr[s][i] == 1 and visited[i] == 0:
            dfs_pre(i)


def dfs_post(s):
    global visited
    visited[s] = 1
    for i in range(N, 0, -1):
        if arr[s][i] == 1 and visited[i] == 0:
            dfs_post(i)
    else:
        print(s, end=' ')


visited = [0] * (N+1)
dfs_pre(S)
print()
visited = [0] * (N+1)
dfs_post(S)
