T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    sy = sx = 0
    for n1 in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)
        for n2 in range(N):
            if lst[n2] == 2:
                sy, sx = n1, n2
    print(arr, sy, sx)