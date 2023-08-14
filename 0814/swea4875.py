T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    stack = []
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                visited[i][j] = 1
                while ans != 1:
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 3:
                                ans = 1
                                break
                            elif arr[ni][nj] == 0 and visited[ni][nj] == 0:
                                stack.append((i, j))
                                i, j = ni, nj
                                visited[i][j] = 1
                                break
                    else:
                        if stack:
                            i, j = stack.pop()
                        else:
                            break
    print(f'#{tc}', ans)
