move = [
    [(0, 1), (-1, 0), (-1, 0), (1, 0)],  # 상
    [(0, -1), (1, 0), (0, 1), (-1, 0)],  # 하
    [(-1, 0), (0, -1), (1, 0), (0, 1)],  # 좌
    [(1, 0), (0, 1), (0, -1), (0, -1)]   # 우
]


def robot(y, x, dir):
    if arr[y][x] == 0:
        for dy, dx in move[dir]:
            ny, nx = y + dy, x + dx
            if arr[ny][nx] % 100 == 0:
                arr[y][x] = 10


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
