T = int(input())


def f(i, n, s):
    global min_sum
    if s > min_sum:
        return
    elif i == n:
        min_sum = s
    else:
        for j in range(i, n):
            A[i], A[j] = A[j], A[i]
            s += arr[i][A[i]]
            f(i + 1, n, s)
            s -= arr[i][A[i]]
            A[i], A[j] = A[j], A[i]


def dfs(idx, now_sum):
    global min_sum2
    if now_sum >= min_sum2:
        return
    if idx == N:
        if min_sum2 > now_sum:
            min_sum2 = now_sum
            return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(idx + 1, now_sum + arr[idx][i])
            used[i] = 0


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    A = [i for i in range(N)]
    min_sum = 10 * N
    f(0, N, 0)
    print(f'#{tc}', min_sum)

    used = [0] * N
    min_sum2 = 10 * N
    dfs(0, 0)
    print(min_sum2)
