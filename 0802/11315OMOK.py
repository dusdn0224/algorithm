T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    check = 0
    # omok = ['o'] * 5

    for i in range(N):
        for j in range(N):
            # case = []

            omok = 0
            for di in range(5):
                ni = i + di
                if 0 <= ni < N:
            #         case.append(arr[ni][j])
            # if case == omok:
            #     check += 1
            # case.clear()
                    if arr[ni][j] == 'o':
                        omok += 1
            if omok == 5:
                check += 1

            omok = 0
            for dj in range(5):
                nj = j + dj
                if 0 <= nj < N:
            #         case.append(arr[i][nj])
            # if case == omok:
            #     check += 1
            # case.clear()
                    if arr[i][nj] == 'o':
                        omok += 1
            if omok == 5:
                check += 1

            omok = 0
            for di, dj in [(d, d) for d in range(5)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
            #         case.append(arr[ni][nj])
            # if case == omok:
            #     check += 1
            # case.clear()
                    if arr[ni][nj] == 'o':
                        omok += 1
            if omok == 5:
                check += 1

            omok = 0
            for di, dj in [(d, -d) for d in range(5)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
            #         case.append(arr[ni][nj])
            # if case == omok:
            #     check += 1
            # case.clear()
                    if arr[ni][nj] == 'o':
                        omok += 1
            if omok == 5:
                check += 1

    if check > 0:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
