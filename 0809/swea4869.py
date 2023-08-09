T = int(input())


def tape(n):
    if n == 10:
        return 1
    # n / 10이 홀수일 때 (30, 50, 70, ...)
    elif (n / 10) % 2:
        return tape(n-10) * 2 - 1
    # n / 10이 짝수일 때 (20, 40, 60, ...)
    else:
        return tape(n-10) * 2 + 1


for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}', tape(N))
