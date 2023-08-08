N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

# arr1.sort()
# dict1 = {}
# for i in arr2:
#     start = 0
#     end = len(arr1) - 1
#     ans = 0
#     while start <= end:
#         mid = (start + end) // 2
#         if arr1[mid] == i:
#             ans += 1
#             arr1.pop(mid)
#             start = 0
#             end = len(arr1) - 1
#         elif arr1[mid] > i:
#             end = mid - 1
#         else:
#             start = mid + 1
#     dict1.setdefault(i, ans)
#     print(dict1[i], end=' ')

dict1 = {}
for i in arr1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
for i in arr2:
    print(dict1.get(i, 0), end=' ')

'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10 10
'''