N = int(input())
arr = list(map(int, input().split()))
x = y = min_x = min_y = 0
arr.sort()
min_mix = 2000000000
for i in range(N-1):
    start = i + 1
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        mix = arr[mid] + arr[i]
        # if mix == 0:
        #     x, y = i, mid
        #     break
        # elif mix > 0:
        #     end = mid - 1
        #     x, y = i, end
        # else:
        #     start = mid + 1
        #     x, y = i, mid
    if min_mix > abs(mix):
        min_mix = abs(mix)
        min_x, min_y = x, y
if arr[min_x] < arr[min_y]:
    print(arr[min_x], arr[min_y])
else:
    print(arr[min_y], arr[min_x])
