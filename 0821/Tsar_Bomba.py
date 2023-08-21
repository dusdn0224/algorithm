T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_virus = 0
    for i in range(N):
        for j in range(N):
            virus = arr[i][j]
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                for k in range(1, P+1):
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < N and 0 <= nj < N:
                        virus += arr[ni][nj]
            if max_virus < virus:
                max_virus = virus
    print(f'#{tc}', max_virus)
