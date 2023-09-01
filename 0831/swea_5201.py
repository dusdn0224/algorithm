T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    V = list(map(int, input().split()))
    W.sort(reverse=True)
    V.sort(reverse=True)
    w = v = 0
    move = 0
    while w < N and v < M:
        if W[w] <= V[v]:
            move += W[w]
            w, v = w+1, v+1
        else:
            w += 1
    print(f'#{tc}', move)
