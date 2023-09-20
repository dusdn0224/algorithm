def dfs(now, lst, d):
    lst[now] = d
    for i in connect[now]:
        if not lst[i]:
            dfs(i, lst, d + arr[now][i])


N, one, two = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
connect = [[] for _ in range(N+1)]
for _ in range(N-1):
    n = list(map(int, input().split()))
    arr[n[0]][n[1]] = arr[n[1]][n[0]] = n[2]
    connect[n[0]].append(n[1])
    connect[n[1]].append(n[0])
d_one = [0] * (N+1)
d_two = [0] * (N+1)
dfs(one, d_one, 0)
dfs(two, d_two, 0)
d_one[one] = d_two[two] = 0
ans = 1000 ** 2
for n in range(1, N+1):
    for m in connect[n]:
        dis = d_one[n] + d_two[m]
        ans = min(ans, dis)
print(ans)