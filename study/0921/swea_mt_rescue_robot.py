T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tunnel = [list(map(int, input().split())) for _ in range(M)]
    for _ in range(M):
        ay, ax, by, bx, C = map(int, input().split())
