def f(y, x, cnt, string):
    if cnt == 7:
        ans.add(string)
        return
    for ny, nx in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
        if 0 <= ny < 4 and 0 <= nx < 4:
            f(ny, nx, cnt+1, string + arr[ny][nx])


T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            f(i, j, 0, '')
    print(f'#{tc}', len(ans))