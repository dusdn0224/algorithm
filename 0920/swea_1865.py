def f(cnt, p, lst):
    global ans
    if cnt == N:
        ans = max(ans, p)
        return
    if p <= ans:
        return
    for i in range(N):
        if i not in lst:
            lst.append(i)
            f(cnt + 1, p * (arr[cnt][i] / 100), lst)
            lst.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    f(0, 1, [])
    ans *= 100
    print(f'#{tc} {ans:.6f}')