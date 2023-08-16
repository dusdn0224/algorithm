T = int(input())


def rsp(a, b):
    if a == b:
        return card[a], a
    elif b - a == 1:
        p = card[a]
        q = card[b]
        if (p, q) == (1, 2) or (p, q) == (2, 3) or (p, q) == (3, 1):
            return q, b
        else:
            return p, a
    else:
        p, wa = rsp(a, (a+b) // 2)
        q, wb = rsp((a+b) // 2 + 1, b)
        if (p, q) == (1, 2) or (p, q) == (2, 3) or (p, q) == (3, 1):
            return q, wb
        else:
            return p, wa


for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    c, w = rsp(0, N - 1)
    print(f'#{tc}', w + 1)
