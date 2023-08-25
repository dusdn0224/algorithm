T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    can = []
    for i in range(1, N-1):
        for j in range(i+1, N):
            S = carrot[:i]
            M = carrot[i:j]
            L = carrot[j:]
            if S[-1] == M[0] or M[-1] == L[0]:
                continue
            if len(S) * len(M) * len(L) == 0:
                continue
            if len(S) > N // 2 or len(M) > N // 2 or len(L) > N // 2:
                continue
            can.append(max(abs(len(S) - len(M)), abs(len(M) - len(L)), abs(len(L) - len(S))))
    try:
        print(f'#{tc}', min(can))
    except:
        print(f'#{tc}', -1)
