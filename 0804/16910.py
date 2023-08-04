T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = N * 2 + 1
    for i in range(1, N + 1):
        cnt += (int((N ** 2 - i ** 2) ** (1 / 2)) * 2 + 1) * 2
    print(f'#{tc}', cnt)
