N, M = map(int, input().split())
card = list(map(int, input().split()))
A = [i for i in range(N)]
min_m = 9 ** M
min_card = []
stack = []


def f(i, n, m, s, c):
    global min_card, min_m, stack
    if i == m:
        if min_m > s:
            min_m = s
            min_card = stack[:]
    else:
        for j in range(c, n):
            stack.append(card[j])
            s *= card[j]
            c += 1
            f(i + 1, n, m, s, c)
            s /= card[j]
            stack.pop()


f(0, N, M, 1, 0)
min_card.sort()
print(*min_card)
