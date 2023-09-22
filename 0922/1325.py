from collections import deque

'''
def f(lst, now):
    global total
    total += hack[now] if hack[now] else len(lst)
    for i in lst:
        f(graph[i], i)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
hack = [0] * (N+1)
for k in range(1, N+1):
    total = 0
    f(graph[k], k)
    hack[k] = total
max_com = 0
ans = []
for n in range(1, N+1):
    if max_com < hack[n]:
        max_com = hack[n]
        ans = [n]
    elif max_com == hack[n]:
        ans.append(n)
print(*ans)
'''
#############################

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
max_v = 0
ans = []
for i in range(1, N+1):
    q = deque()
    q.append(i)
    visited = [0] * (N+1)
    visited[i] = 1
    cnt = 0
    while q:
        t = q.popleft()
        cnt += 1
        for j in graph[t]:
            if not visited[j]:
                visited[j] = visited[t] + 1
                q.append(j)
    if max_v < cnt:
        max_v = cnt
        ans = [i]
    elif max_v == cnt:
        ans.append(i)
print(*ans)