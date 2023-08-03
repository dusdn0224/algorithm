T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # arr = [list(map(int, input().split())) for _ in range(N)]
    # purple = 0
    # for red in arr:
    #     if red[4] == 1:
    #         for blue in arr:
    #             if blue[4] == 2:
    #                 for i in range(red[0], red[2]+1):
    #                     for j in range(red[1], red[3]+1):
    #                         for p in range(blue[0], blue[2]+1):
    #                             for q in range(blue[1], blue[3]+1):
    #                                 if (i, j) == (p, q):
    #                                     purple += 1
    # print(f'#{tc}', purple)

    # 10x10 격자 생성
    arr = [[0] * 10 for _ in range(10)]
    result = 0
    for k in range(N):
        w1, h1, w2, h2, color = map(int, input().split())
        for i in range(w1, w2 + 1):
            for j in range(h1, h2 + 1):
                arr[i][j] += color
                # 격자 값이 3이면 카운트
                if arr[i][j] == 3:
                    result += 1
    print(f'#{tc}', result)
