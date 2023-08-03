T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_f = 0
    # 방의 가로 길이만큼 반복
    for i in range(N):
        cnt = 0
        # 현재 위치의 오른쪽에 있는 모든 상자를 확인
        for j in range(i + 1, N):
            # 현재 위치의 상자가 오른쪽의 상자보다 높이가 크면
            if arr[i] > arr[j]:
                cnt += 1
        # 최대값
        if max_f <= cnt:
            max_f = cnt
    print(f'#{tc}', max_f)

    # max_h = arr[0]
    # fall = 0
    # for i in range(1, N):
    #     if max_h > arr[i]:
    #         fall += 1
    #     else:
    #         max_h = arr[i]
    # print(f'#{tc}', fall)
