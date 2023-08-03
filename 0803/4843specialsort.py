T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        if i % 2 == 0:
            maxidx = i
            for j in range(i + 1, N):
                if arr[maxidx] < arr[j]:
                    maxidx = j
            arr[i], arr[maxidx] = arr[maxidx], arr[i]

        else:
            minidx = i
            for j in range(i + 1, N):
                if arr[minidx] > arr[j]:
                    minidx = j
            arr[i], arr[minidx] = arr[minidx], arr[i]

    # print(f'#{tc}', end=' ')
    # for i in range(10):
    #     print(arr[i], end=' ')
    # print()

    print(f'#{tc}', *arr[:10])
