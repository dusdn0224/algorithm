from collections import deque
T = 10
for tc in range(1, T+1):
    C, S = map(int, input().split())
    graph = [[] for _ in range(101)]
    arr = list(map(int, input().split()))
    for i in range(C // 2):
        graph[arr[2 * i]].append(arr[2 * i + 1])
    visited = [0] * 101
    q = deque()
    q.append(S)
    visited[S] = 1
    while q:
        t = q.popleft()
        for k in graph[t]:
            if not visited[k]:
                q.append(k)
                visited[k] = visited[t] + 1
    max_v = ans = 0
    for n in range(1, 101):
        if max_v <= visited[n]:
            max_v = visited[n]
            ans = n
    print(f'#{tc}', ans)
