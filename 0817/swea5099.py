T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    oven = C[:N]
    Q = [i for i in range(N)]
    p = N - 1
    while len(oven) > 1:
        oven[0] //= 2
        if oven[0] == 0 and p < M - 1:
            oven.pop(0)
            Q.pop(0)
            p += 1
            oven.append(C[p])
            Q.append(p)
        elif oven[0] == 0:
            oven.pop(0)
            Q.pop(0)
        else:
            oven.append(oven.pop(0))
            Q.append(Q.pop(0))
    print(f'#{tc}', Q[0] + 1)
