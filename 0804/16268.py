T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 꽃가루 중 최대값
    max_flower = 0
    # [행][열]
    for i in range(N):
        for j in range(M):
            # 꽃가루
            flower = 0
            # 해당 풍선 + 상하좌우
            for di, dj in [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                # 격자판 안에 있는 경우에만
                if 0 <= ni < N and 0 <= nj < M:
                    flower += arr[ni][nj]
            # 최대값 판단
            if max_flower < flower:
                max_flower = flower

    print(f'#{tc} {max_flower}')
