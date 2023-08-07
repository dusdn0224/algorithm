T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = ''
    for i in range(N):
        for j in range(N):
            if i + M - 1 < N:
                boolean = True
                for s in range(M // 2):
                    if arr[i + s][j] != arr[M - 1 + i - s][j]:
                        boolean = False
                        break
                if boolean:
                    for s in range(M):
                        ans += arr[i + s][j]
            if j + M - 1 < N:
                boolean = True
                for s in range(M // 2):
                    if arr[i][j + s] != arr[i][M - 1 + j - s]:
                        boolean = False
                        break
                if boolean:
                    for s in range(M):
                        ans += arr[i][j + s]
    print(f'#{tc} {ans}')
