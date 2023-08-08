N = int(input())
arr = list(map(int, input().split()))
M = int(input())

start = 1
end = max(arr)

while start <= end:
    budget = 0
    mid = (start + end) // 2
    for i in arr:
        if i >= mid:
            budget += mid
        else:
            budget += i
    if budget > M:
        end = mid - 1
    else:
        start = mid + 1
print(end)
