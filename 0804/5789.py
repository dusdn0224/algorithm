T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]
    boxes = [0] * N
    for i in range(1, Q + 1):
        for j in range(arr[i-1][0] - 1, arr[i-1][1]):
            boxes[j] = i
    print(f'#{tc}', *boxes)
