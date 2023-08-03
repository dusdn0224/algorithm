for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        # arr[arr.index(max(arr))] -= 1
        # arr[arr.index(min(arr))] += 1

        max_idx = 0
        min_idx = 0
        for j in range(1, 100):
            if arr[max_idx] < arr[j]:
                max_idx = j
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[max_idx] -= 1
        arr[min_idx] += 1

    for j in range(1, 100):
        if arr[max_idx] < arr[j]:
            max_idx = j
        if arr[min_idx] > arr[j]:
            min_idx = j

    print(f'#{tc}', arr[max_idx] - arr[min_idx])
