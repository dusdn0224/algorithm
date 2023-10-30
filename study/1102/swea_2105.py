def nemo(q, p, d, cnt):
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    move = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    for y in range(N - 2):
        for x in range(1, N - 1):
            start = (y, x)
            nemo(y, x, 0, 0)
            pass