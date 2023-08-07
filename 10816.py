N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()
for i in arr2:
    start = 0
    end = len(arr1) - 1
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == i:
            ans += 1
            arr1.pop(mid)
            start = 0
            end = len(arr1) - 1
        elif arr1[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    print(ans, end=' ')
