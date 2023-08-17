T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    find = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                visited = [[0] * N for _ in range(N)]
                queue = []
                queue.append((i, j))
                while queue:
                    (p, q) = queue.pop(0)
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = p + di, q + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                                queue.append((ni, nj))
                                visited[ni][nj] = visited[p][q] + 1
                            elif arr[ni][nj] == 3:
                                visited[ni][nj] = visited[p][q]
                                y, x = ni, nj
                                find = True
                                break
                    if find:
                        break
    if find:
        print(f'#{tc}', visited[y][x])
    else:
        print(f'#{tc}', 0)
