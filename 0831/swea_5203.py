def runn(n, player):
    if 0 <= n <= 7:
        if player[n] >= 1 and player[n+1] >= 1 and player[n+2] >= 1:
            return True
    if 1 <= n <= 8:
        if player[n-1] >= 1 and player[n] >= 1 and player[n+1] >= 1:
            return True
    if 2 <= n <= 9:
        if player[n-2] >= 1 and player[n-1] >= 1 and player[n] >= 1:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    A = [0] * 10
    B = [0] * 10
    ans = 0
    for i in range(len(cards)):
        if not i % 2:
            A[cards[i]] += 1
            check = runn(cards[i], A)
            if check or A[cards[i]] >= 3:
                ans = 1
                break
        else:
            B[cards[i]] += 1
            check = runn(cards[i], B)
            if check or B[cards[i]] >= 3:
                ans = 2
                break
    print(f'#{tc}', ans)
