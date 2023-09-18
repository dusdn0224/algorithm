N = int(input())
arr = list(map(int, input().split()))
arr.sort()
K = int(input())
nums = list(map(int, input().split()))
for i in range(K):
    ans = 'X'
    low = 0
    high = N - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == nums[i]:
            ans = 'O'
            break
        elif arr[mid] > nums[i]:
            high = mid - 1
        else:
            low = mid + 1
    print(ans, end='')
