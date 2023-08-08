K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

start = 0
end = max(arr)
ans = 0
while start <= end:
    cut = 0
    mid = (start + end) // 2
    if mid == 0:
        ans = 1
        break
    else:
        for i in arr:
            cut += i // mid
    if cut < N:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid
print(ans)
