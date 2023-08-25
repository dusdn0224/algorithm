T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+2) for _ in range(N+2)]
    arr[N // 2][N // 2] = arr[N // 2 + 1][N // 2 + 1] = 2
    arr[N // 2][N // 2 + 1] = arr[N // 2 + 1][N // 2] = 1
    for _ in range(M):
        j, i, color = map(int, input().split())
        arr[i][j] = color
        for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1),
                       (1, 0), (1, -1), (0, -1), (-1, -1)]:
            ni, nj = i + di, j + dj
            temp = []
            while arr[ni][nj] == color % 2 + 1:
                temp.append((ni, nj))
                ni, nj = ni + di, nj + dj
            if arr[ni][nj] == color:
                for p, q in temp:
                    arr[p][q] = color
    bcnt = wcnt = 0
    for c in arr:
        bcnt += c.count(1)
        wcnt += c.count(2)
    print(f'#{tc}', bcnt, wcnt)
