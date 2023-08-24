T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    n = 0
    crop = 0
    while n < N // 2:
        for i in range(N // 2 - n, N // 2 + n + 1):
            crop += arr[i][n]
            crop += arr[i][N - 1 - n]
        n += 1
    for i in range(N):
        crop += arr[i][N // 2]
    print(f'#{tc}', crop)
