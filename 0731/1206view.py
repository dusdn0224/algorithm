for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    num = 0
    for i in range(2, N-2):
        # if arr[i] >= arr[i-2] and arr[i] >= arr[i-1] and arr[i] >= arr[i+1] and arr[i] >= arr[i+2]:
        #     list1 = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        #     max_h = list1[0]
        #     for j in range(1, 4):
        #         if max_h < list1[j]:
        #             max_h = list1[j]
        #     num += arr[i] - max_h
        list1 = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        max_h = list1[0]
        for j in range(1, 4):
            if max_h < list1[j]:
                max_h = list1[j]
        if max_h <= arr[i]:
            num += arr[i] - max_h

    print(f'#{tc}', num)
