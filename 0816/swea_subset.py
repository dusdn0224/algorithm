T = int(input())


def subset(i, n, s):
    global cnt
    if s > S:
        return
    elif i == n:
        if s == S:
            cnt += 1
    else:
        subset(i + 1, n, s + arr[i])
        subset(i + 1, n, s)


for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    subset(0, N, 0)
    print(f'#{tc}', cnt)
