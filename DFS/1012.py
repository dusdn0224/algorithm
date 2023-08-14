T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        k1, k2 = map(int, input().split())
        arr[k2][k1] = 1

    stack = []
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                while True:
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M:
                            if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                                stack.append((i, j))
                                i, j = ni, nj
                                visited[i][j] = 1
                                break
                    else:
                        if stack:
                            i, j = stack.pop()
                        else:
                            break
                cnt += 1
    print(cnt)
