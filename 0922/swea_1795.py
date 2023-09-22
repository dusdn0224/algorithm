import heapq
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append([y, c])
    max_dist = 0
    distance = [9e9] * (N+1)
    distance[X] = 0
    heap = []
    heapq.heappush(heap, (0, X))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue

        distance2 = [9e9] * (N + 1)
        distance2[now] = 0
        heap2 = []
        heapq.heappush(heap2, (0, now))
        while heap2:
            dist2, now2 = heapq.heappop(heap2)
            if distance2[now2] < dist2:
                continue
            if now2 == X:
                max_dist = max(max_dist, dist + dist2)
                break
            for nxt2 in graph[now2]:
                if distance2[nxt2[0]] <= dist2 + nxt2[1]:
                    continue
                distance2[nxt2[0]] = dist2 + nxt2[1]
                heapq.heappush(heap2, (dist2 + nxt2[1], nxt2[0]))

        for nxt in graph[now]:
            if distance[nxt[0]] <= dist + nxt[1]:
                continue
            distance[nxt[0]] = dist + nxt[1]
            heapq.heappush(heap, (dist + nxt[1], nxt[0]))
    print(f'#{tc}', max_dist)