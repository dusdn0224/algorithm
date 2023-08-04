T = int(input())
for tc in range(1, T+1):
    N = int(input())
    facto = []
    for i in [2, 3, 5, 7, 11]:
        n = -1
        r = 0
        k = N
        while r == 0:
            n += 1
            r = k % i
            k /= i
        facto.append(n)
    print(f'#{tc}', *facto)
