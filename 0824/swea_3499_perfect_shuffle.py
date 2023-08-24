T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(input().split())
    if N % 2:
        result = []
        for i in range(N // 2):
            result.append(card[i])
            result.append(card[i + N // 2 + 1])
        result.append(card[N // 2])
    else:
        result = []
        for i in range(N // 2):
            result.append(card[i])
            result.append(card[i + N // 2])
    print(f'#{tc}', *result)
