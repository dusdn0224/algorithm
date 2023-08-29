T = int(input())
for tc in range(1, T+1):
    N, W = map(int, input().split())
    window = list(map(int, input().split()))
    for i in range(N - W + 1):
        point = 0
        for num in window[i:i+W]:
            point += num
        if i == 0:
            max_point = point
            start = 0
        else:
            if max_point < point:
                max_point = point
                start = i
    print(f'#{tc}', start, start + W - 1, max_point)
