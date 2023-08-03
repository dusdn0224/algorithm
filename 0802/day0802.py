# N = 2  # 행
# M = 4  # 열
#
# arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j + (M-1 - 2*j) * (i % 2)])
#
# # 행의 합(최대값)
# max_v = 0
# for i in range(N):
#     row_total = 0
#     for j in range(M):
#         row_total += arr[i][j]
#     if max_v < row_total:
#         max_v = row_total
#
# arr = [[0] * M for _ in range(N)]  # [[0, 0, 0, 0], [0, 0, 0, 0]]
# arr2 = [[0] * M] * N  # [[0, 0, 0, 0], [0, 0, 0, 0]]
# arr[0][0] = 1  # [[1, 0, 0, 0], [0, 0, 0, 0]]
# arr2[0][0] = 1  # [[1, 0, 0, 0], [1, 0, 0, 0]]

# """
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# """
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# # 자기 자신과 주위 값들의 합(최대값)
# max_v = 0  # 모든 원소가 0 이상이라면
# for i in range(N):  # 모든 원소 arr[i][j]에 대해
#     for j in range(N):
#         s = arr[i][j]
#         for k in range(4):
#             ni, nj = i + di[k], j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:  # 배열을 벗어나지 않으면
#                 s += arr[ni][nj]
#         # 여기까지 주변 원소를 포함한 합
#         if max_v < s:
#             max_v = s
# print(max_v)

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# total1 = 0
# for i in range(N):
#     total1 += arr[i][i]
# total2 = 0
# for i in range(N):
#     total2 += arr[i][N-1-i]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
s = 0
for i in range(N):
    for j in range(N):
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                s += abs(arr[i][j] - arr[ni][nj])
print('<연습문제1>', s)
