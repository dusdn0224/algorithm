T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 꽃가루 중 최대값
    max_flower = 0
    # [행][열]
    for i in range(N):
        for j in range(M):
            # 해당 풍선 꽃가루 = 상하좌우 추가로 터질 풍선 개수
            flower = K = arr[i][j]
            # 상하좌우
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # 몇개씩?
                for k in range(1, K + 1):
                    ni, nj = i + di * k, j + dj * k
                    # 격자판 안에 있는 경우에만
                    if 0 <= ni < N and 0 <= nj < M:
                        flower += arr[ni][nj]
            # 최대값 판단
            if max_flower < flower:
                max_flower = flower

    print(f'#{tc} {max_flower}')
