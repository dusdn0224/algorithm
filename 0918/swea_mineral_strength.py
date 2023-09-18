N, Q = map(int, input().split())
ST = list(map(int, input().split()))
for _ in range(Q):
    cnt = 0
    S, E = map(int, input().split())
    for st in ST:
        if S <= st <= E:
            cnt += 1
    print(cnt)
