def f():
    pass


def bfs(y, x):
    visited = [0] * N
    visited[y] = 1
    q = [y]
    while q:
        t = q.pop(0)
        if t == x:
            return True
        else:
            for i in range(N):
                if arr[t][i] and not visited[i]:
                    q.append(i)
                    visited[i] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    population = list(map(int, input().split()))
