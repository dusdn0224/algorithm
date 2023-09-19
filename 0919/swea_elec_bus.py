T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    arr2 = [0] * arr[0]
    for i in range(1, arr[0]):
        arr2[i] = i + arr[i]
    cnt = 0
    now = 1
    far = arr2[1]
    while True:
        for k in range(far, now, -1):
            if far < arr2[k]:
                far = arr2[k]
                now = k
        cnt += 1
        if far >= arr[0]:
            break
    print(f'#{tc}', cnt)