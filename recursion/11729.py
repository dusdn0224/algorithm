N = int(input())
cnt = 0
arr = []


def hanoi(n, s, e, r):
    global cnt
    if n == 1:
        # print(s, e)
        arr.append([s, e])
        cnt += 1
    else:
        hanoi(n-1, s, r, e)
        # print(s, e)
        arr.append([s, e])
        cnt += 1
        hanoi(n-1, r, e, s)


hanoi(N, 1, 3, 2)
print(cnt)
for i in range(len(arr)):
    print(*arr[i])
