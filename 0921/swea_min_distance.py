import heapq
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])
    distance = [9e9] * (N+1)
    heap = []
    heapq.heappush(heap, (0, 0))
    distance[0] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            if distance[next[0]] <= dist + next[1]:
                continue
            distance[next[0]] = dist + next[1]
            heapq.heappush(heap, (dist + next[1], next[0]))
    print(f'#{tc}', distance[N])