T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # stop_list = [0] * (N+1)
    # for stop in arr:
    #     stop_list[stop] = 1
    #
    # battery = K
    # charge = 0
    # for i in range(1, N + 1):
    #     battery -= 1
    #     if stop_list[i] == 1:
    #         try:
    #             if battery >= stop_list.index(1, i + 1) - i:
    #                 continue
    #             else:
    #                 battery = K
    #                 charge += 1
    #         except ValueError:
    #             if battery < N - i:
    #                 battery = K
    #                 charge += 1
    #     if i != N and battery == 0:
    #         charge = 0
    #         break
    # print(f'#{tc}', charge)

    # curr: 현재 위치, cnt: 충전 횟수
    curr = cnt = 0
    # 종점 도착할 때까지 반복
    while curr != N:
        # curr + K: 한번 충전으로 갈 수 있는 거리, N: 종점까지의 거리
        if N <= curr + K:
            curr = N
            break
        # 충전소 뒤에서부터 순회
        for i in range(len(arr) - 1, -1, -1):
            # 리스트 arr 의 값이 curr + K 이내에 있다면
            if arr[i] <= curr + K:
                cnt += 1
                curr = arr[i]
                arr = arr[i + 1:]
                break
            # 충전소를 찾지 못했다면
            if i == 0:
                cnt = 0
                curr = N  # 현재 위치를 종점으로
    print(f'#{tc} {cnt}')
