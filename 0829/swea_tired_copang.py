def bfs(p1, p2, k1, k2):
    q = [(p1, p2)]


N = int(input())
V = [list(map(int, input().split())) for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
