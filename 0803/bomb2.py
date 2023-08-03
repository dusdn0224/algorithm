N, M = map(int, input().split())
K = int(input())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '@':
            arr[i][j] = '%'
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                for k in range(1, K+1):
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == '#':
                            break
                        elif arr[ni][nj] == '_':
                            arr[ni][nj] = '%'

print(arr)
