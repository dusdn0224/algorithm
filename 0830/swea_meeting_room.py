N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
arr.sort(key=lambda x: x[1])
cnt = 1
temp = arr[0][1]
for i in range(1, N):
    if temp <= arr[i][0]:
        temp = arr[i][1]
        cnt += 1
print(cnt)
