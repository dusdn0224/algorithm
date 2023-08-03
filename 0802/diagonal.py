# N = int(input())
# arr1 = [list(map(int, input().split())) for _ in range(N)]
#
# y1 = x1 = 0
# max1 = 0
# for i in range(N):
#     for j in range(N):
#         s = 0
#         for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 s += arr1[ni][nj]
#         if max1 < s:
#             max1 = s
#             y1, x1 = i, j
# print(y1, x1)


def sum_diagonal(y, x, arr):
    sum_d = 0
    for dy, dx in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(arr) and 0 <= nx < len(arr):
            sum_d += arr[ny][nx]
    return sum_d


arr2 = [
    [3, 3, 5, 3, 1],
    [2, 2, 4, 2, 6],
    [4, 9, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 3, 5, 9, 2]
]

max2 = 0
y2 = x2 = 0
for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        case = sum_diagonal(i, j, arr2)
        if max2 < case:
            max2 = case
            y2, x2 = i, j
print(y2, x2)
