from collections import deque
N, K = map(int, input().split())
q = deque()
q.append(N)
visited = [-1] * 500001
visited[N] = 0
while q:
    now = q.popleft()
    turn = visited[now]
    if now == K + (turn * (turn + 1) // 2):
        break
    for nxt in [now - 1, now + 1, now * 2]:
        if 0 <= nxt <= 500000:
            visited[nxt] = turn + 1
            q.append(nxt)
print(turn)