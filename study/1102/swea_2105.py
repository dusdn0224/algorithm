def nemo(q, p, d, lst):
    global max_cnt
    if d == 0 or d == 1 or d == 2:
        nq1, np1 = q + move[d][0], p + move[d][1]
        if start_y < nq1 < N and 0 <= np1 < N and arr[nq1][np1] not in lst:
            lst.append(arr[nq1][np1])
            nemo(nq1, np1, d, lst)
            lst.pop()

        nq2, np2 = q + move[d+1][0], p + move[d+1][1]
        if nq2 == start_y and np2 == start_x:
            max_cnt = max(max_cnt, len(lst))
            return
        if start_y < nq2 < N and 0 <= np2 < N and arr[nq2][np2] not in lst:
            lst.append(arr[nq2][np2])
            nemo(nq2, np2, d+1, lst)
            lst.pop()
    elif d == 3:
        nq, np = q + move[d][0], p + move[d][1]
        if nq == start_y and np == start_x:
            max_cnt = max(max_cnt, len(lst))
            return
        if start_y < nq < N and 0 <= np < N and arr[nq][np] not in lst:
            lst.append(arr[nq][np])
            nemo(nq, np, d, lst)
            lst.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    move = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    max_cnt = 0
    for y in range(N - 2):
        for x in range(1, N - 1):
            start_y, start_x = y, x
            nemo(y, x, 0, [arr[y][x]])
    print(f'#{tc}', max_cnt if max_cnt else -1)
