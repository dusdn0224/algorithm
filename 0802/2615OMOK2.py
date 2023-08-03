arr = [list(map(int, input().split())) for _ in range(19)]
board = [[0] * 21 for _ in range(21)]
for i in range(19):
    for j in range(19):
        board[i + 1][j + 1] = arr[i][j]

check = 0
x = y = 0
for i in range(1, 20):
    for j in range(1, 20):

        omok = 0
        for di in range(5):
            ni = i + di
            if 1 <= ni <= 19:
                if board[ni][j] == 1:
                    omok += 1
                elif board[ni][j] == 2:
                    omok += 10
        if omok % 10 == 5:
            if board[i + 5][j] != 1 and board[i - 1][j] != 1:
                check += 1
                x, y = i, j
        elif omok // 10 == 5:
            if board[i + 5][j] != 2 and board[i - 1][j] != 2:
                check += 10
                x, y = i, j

        omok = 0
        for dj in range(5):
            nj = j + dj
            if 1 <= nj <= 19:
                if board[i][nj] == 1:
                    omok += 1
                elif board[i][nj] == 2:
                    omok += 10
        if omok % 10 == 5:
            if board[i][j + 5] != 1 and board[i][j - 1] != 1:
                check += 1
                x, y = i, j
        elif omok // 10 == 5:
            if board[i][j + 5] != 2 and board[i][j - 1] != 2:
                check += 10
                x, y = i, j

        omok = 0
        for di, dj in [(d, d) for d in range(5)]:
            ni, nj = i + di, j + dj
            if 1 <= ni <= 19 and 1 <= nj <= 19:
                if board[ni][nj] == 1:
                    omok += 1
                elif board[ni][nj] == 2:
                    omok += 10
        if omok % 10 == 5:
            if board[i + 5][j + 5] != 1 and board[i - 1][j - 1] != 1:
                check += 1
                x, y = i, j
        elif omok // 10 == 5:
            if board[i + 5][j + 5] != 2 and board[i - 1][j - 1] != 2:
                check += 10
                x, y = i, j

        omok = 0
        for di, dj in [(d, -d) for d in range(5)]:
            ni, nj = i + di, j + dj
            if 1 <= ni <= 19 and 1 <= nj <= 19:
                if board[ni][nj] == 1:
                    omok += 1
                elif board[ni][nj] == 2:
                    omok += 10
        if omok % 10 == 5:
            if board[i + 5][j - 5] != 1 and board[i - 1][j + 1] != 1:
                check += 1
                x, y = i + 4, j - 4
        elif omok // 10 == 5:
            if board[i + 5][j - 5] != 2 and board[i - 1][j + 1] != 2:
                check += 10
                x, y = i + 4, j - 4

if check % 10 > 0:
    print(1)
    print(x, y)
elif check // 10 > 0:
    print(2)
    print(x, y)
else:
    print(0)
