def f(now, pattern):
    if pattern == 1:
        if arr[now][1] != -1:
            f(arr[now][1], 1)
        print(now, end=' ')
        if arr[now][2] != -1:
            f(arr[now][2], 1)
    elif pattern == 2:
        print(now, end=' ')
        if arr[now][1] != -1:
            f(arr[now][1], 2)
        if arr[now][2] != -1:
            f(arr[now][2], 2)
    elif pattern == 3:
        if arr[now][1] != -1:
            f(arr[now][1], 3)
        if arr[now][2] != -1:
            f(arr[now][2], 3)
        print(now, end=' ')


N = int(input())
arr = [[0, -1, -1]]
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()
f(1, 1)
print()
f(1, 2)
print()
f(1, 3)
