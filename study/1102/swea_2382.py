def move(dt):
    new = dict()
    keys = list(dt.keys())
    many = []
    for key in keys:
        p, q = key
        n, direc = dt[key]

        if direc == 1:
            p -= 1
        elif direc == 2:
            p += 1
        elif direc == 3:
            q -= 1
        elif direc == 4:
            q += 1

        if p in (0, N-1) or q in (0, N-1):
            n[0] //= 2
            direc = reverse[direc]

        if not new.get((p, q)):
            new.setdefault((p, q), [n, direc])

        else:
            if n[0] > max(new[(p, q)][0]):
                new[(p, q)][1] = direc
            new[(p, q)][0].append(n[0])
            many.append((p, q))

    for m in many:
        new[m][0] = [sum(new[m][0])]

    return new


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    location = dict()
    for _ in range(K):
        y, x, num, d = map(int, input().split())
        location.setdefault((y, x), [[num], d])
    reverse = [0, 2, 1, 4, 3]
    for _ in range(M):
        location = move(location)
    ans = 0
    for value in list(location.values()):
        ans += value[0][0]
    print(f'#{tc}', ans)