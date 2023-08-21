T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_nemo = cnt = 0
    for i in range(N):
        for j in range(N):
            for p in range(i, N):
                for q in range(j, N):
                    if arr[i][j] == arr[p][q]:
                        nemo = (p - i + 1) * (q - j + 1)
                        if max_nemo < nemo:
                            max_nemo = nemo
                            cnt = 1
                        elif max_nemo == nemo:
                            cnt += 1
    print(f'#{tc}', cnt)
