T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 단어가 들어갈 수 있는 자리의 수
    ans = 0
    for i in range(N):
        # 행 우선 순회
        white = 0
        for j in range(N):
            # 연속한 빈 칸의 개수
            if arr[i][j]:
                white += 1
            # 막힌 칸이 나오면 초기화
            else:
                white = 0
            # 맨 끝이거나 다음 칸이 막혀 있을때 빈 칸이 K개 라면
            if (j == N - 1 or arr[i][j + 1] == 0) and white == K:
                ans += 1

        # 열 우선 순회
        white = 0
        for j in range(N):
            # 연속한 빈 칸의 개수
            if arr[j][i]:
                white += 1
            # 막힌 칸이 나오면 초기화
            else:
                white = 0
            # 맨 끝이거나 다음 칸이 막혀 있을때 빈 칸이 K개 라면
            if (j == N - 1 or arr[j + 1][i] == 0) and white == K:
                ans += 1

    print(f'#{tc} {ans}')
