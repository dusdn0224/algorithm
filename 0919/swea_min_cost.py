def f(cnt, hap, lst):
    global min_hap
    if cnt == N:
        min_hap = min(min_hap, hap)
        return
    if hap > min_hap:
        return
    for i in range(N):
        if i not in lst:
            lst.append(i)
            f(cnt + 1, hap + arr[cnt][i], lst)
            lst.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_hap = 100 * 15
    f(0, 0, [])
    print(f'#{tc}', min_hap)