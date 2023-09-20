def dfs_low(now):
    global cnt_low
    for i in range(1, N+1):
        if arr[now][i]:
            dfs_low(i)
            cnt_low += 1


def dfs_high(now):
    global cnt_high
    for i in range(1, N+1):
        if arr[i][now]:
            dfs_high(i)
            cnt_high += 1


N, M, X = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    m1, m2 = map(int, input().split())
    arr[m1][m2] = 1
cnt_low = 0
cnt_high = 0
dfs_low(X)
dfs_high(X)
print(1 + cnt_high)
print(N - cnt_low)