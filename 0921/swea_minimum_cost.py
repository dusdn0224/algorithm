from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited = [[9e9] * N for _ in range(N)]
    visited[0][0] = 0
    lst = []
    while q:
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                chai = arr[ny][nx] - arr[y][x]
                if chai < 0:
                    chai = 0
                fuel = visited[y][x] + 1 + chai
                if visited[ny][nx] > fuel:
                    visited[ny][nx] = fuel
                    q.append((ny, nx))
    print(f'#{tc}', visited[N-1][N-1])
