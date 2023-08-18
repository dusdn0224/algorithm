N, M, V = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    m1, m2 = map(int, input().split())
    arr[m1][m2] = arr[m2][m1] = 1

visited_dfs = [0] * (N + 1)
def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in range(1, N + 1):
        if arr[v][i] and not visited_dfs[i]:
            dfs(i)


def bfs(v):
    visited_bfs = [0] * (N + 1)
    Q = list()
    Q.append(v)
    visited_bfs[v] = 1
    while Q:
        t = Q.pop(0)
        print(t, end=' ')
        for i in range(1, N + 1):
            if arr[t][i] and not visited_bfs[i]:
                Q.append(i)
                visited_bfs[i] = 1


dfs(V)
print()
bfs(V)
