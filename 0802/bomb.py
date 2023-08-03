# arr1 = [['_'] * 5 for i in range(4)]
#
#
# def bomb(y, x, arr):
#     for dy, dx in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
#         ny, nx = y + dy, x + dx
#         if 0 <= ny < len(arr) and 0 <= nx < len(arr[0]):
#             arr[ny][nx] = '#'
#
#
# for _ in range(2):
#     i, j = map(int, input().split())
#     bomb(i, j, arr1)
# for i in range(len(arr1)):
#     print(arr1[i])

print(list(range(-5, -1)))
