from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [[-1] * M for _ in range(N)]
    q = deque()
    for i in range(N):
        a = list(input())
        for j in range(M):
            if a[j] == 'W':
                q.append((i, j))
                visited[i][j] = 0
    ans = 0
    while q:
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == -1:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    ans += visited[ny][nx]
    print(f'#{tc}', ans)
