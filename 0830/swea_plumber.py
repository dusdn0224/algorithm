N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 1
now = arr[0]
for i in range(1, N):
    if arr[i] - now < L:
        continue
    else:
        cnt += 1
        now = arr[i]
print(cnt)
