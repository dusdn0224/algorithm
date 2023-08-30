def visit(y, x):
    global cnt
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == arr[y][x] + 1:
            cnt += 1
            visit(ny, nx)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # ans = [N ** 2 + 1, 0]
    # for i in range(N):
    #     for j in range(N):
    #         cnt = 1
    #         visit(i, j)
    #         if ans[1] < cnt:
    #             ans = [arr[i][j], cnt]
    #         elif ans[1] == cnt:
    #             ans[0] = min(ans[0], arr[i][j])
    # print(f'#{tc}', *ans)

    ans = [N ** 2 + 1, 0]
    for i in range(N):
        for j in range(N):
            cnt = 1
            while True:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
                        cnt += 1
                        i, j = ni, nj
                        break
                else:
                    break
            if ans[1] < cnt:
                ans = [arr[i][j] - cnt + 1, cnt]
            elif ans[1] == cnt:
                ans[0] = min(ans[0], arr[i][j] - cnt + 1)
    print(f'#{tc}', *ans)
