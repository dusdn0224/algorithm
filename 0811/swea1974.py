T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):
        column = set()
        for j in range(9):
            column.add(arr[i][j])
        if len(column) != 9:
            ans = 0
            break
        row = set()
        for j in range(9):
            row.add(arr[j][i])
        if len(row) != 9:
            ans = 0
            break
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = set()
            for p in range(3):
                for q in range(3):
                    square.add(arr[i + p][j + q])
            if len(square) != 9:
                ans = 0
                break
        if ans == 0:
            break
    print(f'#{tc}', ans)
