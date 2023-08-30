def dfs(y, x, hap):
    global min_hap
    if (y, x) == (N - 1, N - 1):
        min_hap = min(min_hap, hap)
    elif min_hap <= hap:
        return
    else:
        for dy, dx in [(0, 1), (1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                dfs(ny, nx, hap + arr[ny][nx])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_hap = 10 * 13 * 13
    dfs(0, 0, arr[0][0])
    print(f'#{tc}', min_hap)
