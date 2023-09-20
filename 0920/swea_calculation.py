T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = [N]
    visited = [0] * 1000001
    visited[N] = 1
    while q:
        t = q.pop(0)
        if t == M-1 or t == M+1 or t == M / 2 or t == M + 10:
            break
        for i in [t+1, t-1, t*2, t-10]:
            if 0 < i <= 1000000 and not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1
    print(f'#{tc}', visited[t])
