T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    a = b = 0

    l, r = 1, P
    while l <= r:
        c = int((l + r) / 2)
        a += 1
        if c == Pa:
            break
        elif c > Pa:
            r = c
        else:
            l = c

    l, r = 1, P
    while l <= r:
        c = int((l + r) / 2)
        b += 1
        if c == Pb:
            break
        elif c > Pb:
            r = c
        else:
            l = c

    if a < b:
        print(f'#{tc} A')
    elif a > b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
