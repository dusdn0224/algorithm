def f(ground):
    on_runway = False
    cnt = 1
    i = 1
    while i < N:
        prev = ground[i - 1]
        now = ground[i]
        if abs(now - prev) > 1:
            return False
        if not on_runway:
            if now == prev:
                cnt += 1
                i += 1
            elif now - prev == 1:
                if cnt < X:
                    return False
                else:
                    cnt = 1
                    i += 1
            elif now - prev == -1:
                on_runway = True
                cnt = 1
                i += 1
        else:
            if now == prev:
                cnt += 1
                i += 1
            else:
                return False
            if cnt == X:
                on_runway = False
                cnt = 0
    if not on_runway:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    columns = [[] for _ in range(N)]
    ans = 0
    for _ in range(N):
        row = list(map(int, input().split()))
        if f(row):
            ans += 1
        for x in range(N):
            columns[x].append(row[x])
    for column in columns:
        if f(column):
            ans += 1
    print(f'#{tc}', ans)
