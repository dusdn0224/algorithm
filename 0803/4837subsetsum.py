T = int(input())
A = list(range(1, 13))
a = len(A)
for tc in range(1, T+1):
    N, K = map(int, input().split())
    check = 0

    for i in range(1 << a):
        n = 0
        k = 0
        for j in range(a):
            if i & (1 << j):
                n += 1
                k += A[j]

        if N == n and K == k:
            check += 1

    print(f'#{tc}', check)
