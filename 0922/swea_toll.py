import heapq


def dijk():
    heap = []
    distance = [9e9] * (N+1)
    heapq.heappush(heap, (0, A))
    distance[A] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        if now == B:
            print(dist)
            return
        for nxt in graph[now]:
            if distance[nxt[0]] <= dist + nxt[1]:
                continue
            distance[nxt[0]] = dist + nxt[1]
            heapq.heappush(heap, (dist + nxt[1], nxt[0]))


N, M, K = map(int, input().split())
A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    f, t, c = map(int, input().split())
    graph[f].append([t, c])
    graph[t].append([f, c])
ic = [0]
for _ in range(K):
    ic.append(int(input()))
for i in range(K+1):
    if ic[i]:
        for j in range(1, N+1):
            for lst in graph[j]:
                lst[1] += ic[i]
    dijk()
