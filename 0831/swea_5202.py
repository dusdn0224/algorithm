T = int(input())
for tc in range(1, T+1):
    N = int(input())
    apply = []
    for _ in range(N):
        s, e = map(int, input().split())
        apply.append([e, s])
    apply.sort()
    cnt = 1
    now = apply[0][0]
    for i in range(1, N):
        if now <= apply[i][1]:
            cnt += 1
            now = apply[i][0]
    print(f'#{tc}', cnt)
