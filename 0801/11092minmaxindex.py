T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0  # 최소값의 인덱스
    max_idx = 0  # 최대값의 인덱스
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i

    ans = max_idx - min_idx
    if ans < 0:
        ans = -ans

    print(f'#{tc}', ans)
