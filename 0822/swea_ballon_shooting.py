def lr():
    global balloon
    max_point = 0
    for i in range(1, len(balloon) - 1):
        point = balloon[i - 1] * balloon[i + 1]
        if max_point < point:
            max_point = point
            b = i
    balloon.pop(b)
    return max_point


def dp(n):
    


def f(i, n):
    if i == n:
        for k in order:
            if k == 0:
                point += balloon[1]
            elif k == len(balloon) - 1:
                point +=
    else:
        for j in (i, n -1):
            order[i], order[j] = order[j], order[i]
            f(i+1, N)
            order[i], order[j] = order[j], order[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    balloon = list(map(int, input().split()))
    ans = 0
    for _ in range(N - 2):
        ans += lr()
    ans += max(balloon) * 2
    print(balloon, ans)

    order = [i for i in range(N)]
