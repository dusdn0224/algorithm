N = int(input())
arr = list(map(int, input().split()))
min_mix = 2000000000
x = y = 0
arr.sort()
for i in range(N):
    # for j in range(i+1, N):
    #     if arr[i] + arr[j] >= 0:
    #         mix = arr[i] + arr[j]
    #     else:
    #         mix = -(arr[i] + arr[j])
    #     if min_mix >= mix:
    #         min_mix = mix
    #         x, y = i, j
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] + arr[i] == 0:
            x, y = i, mid
            
if arr[x] < arr[y]:
    print(arr[x], arr[y])
else:
    print(arr[y], arr[x])
