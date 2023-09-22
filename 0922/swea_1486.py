def f(lst, h):
    global min_h
    if h >= B:
        min_h = min(min_h, h)
        return
    for k in range(max(lst) + 1 if lst else 0, N):
        lst.append(k)
        f(lst, h + H[k])
        lst.pop()


def f2(level, h):
    global min_h
    if h >= B:
        min_h = min(min_h, h)
        return
    if level == N:
        return
    f2(level + 1, h + H[level])
    f2(level + 1, h)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_h = 9e9
    # f([], 0)
    f2(0, 0)
    print(f'#{tc}', min_h - B)