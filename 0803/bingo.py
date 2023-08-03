"""
17 6 9 7 20
13 2 10 3 5
15 18 8 12 14
23 19 4 24 25
22 1 21 11 16
23 3 21 18 8
6 24 13 12 10
9 2 5 15 22
4 11 1 7 20
19 16 17 25 14
"""

arr = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]
call = []
for i in range(5):
    for j in range(5):
        call.append(arr2[i][j])


def bingo(board):
    cnt = 0
    for i in range(5):
        # 가로 체크
        b = 0
        for j in range(5):
            if board[i][j] == 1:
                b += 1
        if b == 5:
            cnt += 1
        # 세로 체크
        b = 0
        for j in range(5):
            if board[j][i] == 1:
                b += 1
        if b == 5:
            cnt += 1
    # 대각선 체크(우하향)
    b = 0
    for i in range(5):
        if board[i][i] == 1:
            b += 1
    if b == 5:
        cnt += 1
    # 대각선 체크(우상향)
    b = 0
    for i in range(5):
        if board[i][4-i] == 1:
            b += 1
    if b == 5:
        cnt += 1
    return cnt


bingo_board = [[0] * 5 for _ in range(5)]

for num in call:
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                bingo_board[i][j] = 1
    check = bingo(bingo_board)
    if check == 3:
        print(num)
        break

# arr = [int(num) for _ in range(5) for num in input().split()]
# arr2 = [int(num) for _ in range(5) for num in input().split()]
# cnt = 0
# x_lst = [0] * 10
# y_lst = [0] * 10
# di_lst1 = [0] * 10
# di_lst2 = [0] * 10
# for n in arr2:
#     a = arr.index(n)
#     x, y = a//5, a % 5
#     x_lst[x] += 1
#     y_lst[y] += 1
#     di_lst1[x+y] += 1
#     di_lst2[y-x+4] += 1
#     if x_lst[x] == 5:
#         cnt += 1
#     if y_lst[y] == 5:
#         cnt += 1
#     if di_lst1[x+y] == 5 or di_lst2[y-x+4] == 5:
#         cnt += 1
#     print(x_lst)
#     print(y_lst)
#     print(di_lst1)
#     print(di_lst2)
#     print()
#     if cnt == 3:
#         print(n)
#         break
