N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
start = 0
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for chu in arr:
        cnt += chu // mid
    if cnt >= K:
        start = mid + 1
    else:
        end = mid - 1
print(start - 1)