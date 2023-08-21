T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 2:
                y, x = i, j
    max_d = 0
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 1:
                d = ((i - y) ** 2 + (j - x) ** 2) ** (1 / 2)
                if max_d < d:
                    max_d = d
    if max_d - int(max_d) == 0:
        max_d = int(max_d)
    else:
        max_d = int(max_d) + 1
    print(f'#{tc}', max_d)
