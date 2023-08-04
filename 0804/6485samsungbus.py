T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stop = [int(input()) for _ in range(P)]

    # 전체 정류장
    all_stop = [0] * 5001

    # 각 버스에 대해
    for bus in arr:
        # 서는 정류장 마다 1 더해주기
        for i in range(bus[0], bus[1] + 1):
            all_stop[i] += 1

    print(f'#{tc}', end=' ')
    # 입력받은 P개의 정류장만 출력
    for i in stop:
        print(all_stop[i], end=' ')
    print()
