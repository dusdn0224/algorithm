def f(cnt):
    if cnt == N:
        print(*p)
        return
    if M == 1:
        for num in nums:
            p[cnt] = num
            f(cnt+1)
    elif M == 2:
        for num in nums:
            if num >= max(p):
                p[cnt] = num
                f(cnt+1)
                p[cnt] = 0
    elif M == 3:
        for num in nums:
            if num not in p:
                p[cnt] = num
                f(cnt+1)
                p[cnt] = 0


N, M = map(int, input().split())
nums = [i for i in range(1, 7)]
p = [0] * N
f(0)