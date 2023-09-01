pipe = [
    [0, 0, 0, 0],
    [(-1, 0), (1, 0), (0, -1), (0, 1)],
    [(-1, 0), (1, 0)],
    [(0, -1), (0, 1)],
    [(-1, 0), (0, 1)],
    [(1, 0), (0, 1)],
    [(1, 0), (0, -1)],
    [(-1, 0), (0, -1)],
]   # 파이프 모양 별로 네방향 연결 가능 여부 [상, 하, 좌, 우]
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    q = [(R, C, 1)]
    visited = [[0] * M for _ in range(N)]
    while q:
        y, x, hour = q.pop(0)
        if hour == L + 1:
            break
        visited[y][x] = 1
        for dy, dx in pipe[arr[y][x]]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if (dy, dx) == (-1, 0):
                    if arr[ny][nx] in [1, 2, 5, 6] and not visited[ny][nx]:
                        q.append((ny, nx, hour + 1))
                elif (dy, dx) == (1, 0):
                    if arr[ny][nx] in [1, 2, 4, 7] and not visited[ny][nx]:
                        q.append((ny, nx, hour + 1))
                elif (dy, dx) == (0, -1):
                    if arr[ny][nx] in [1, 3, 4, 5] and not visited[ny][nx]:
                        q.append((ny, nx, hour + 1))
                elif (dy, dx) == (0, 1):
                    if arr[ny][nx] in [1, 3, 6, 7] and not visited[ny][nx]:
                        q.append((ny, nx, hour + 1))
    print(f'#{tc}', sum(sum(visited, [])))
