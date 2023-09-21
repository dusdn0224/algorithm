"""
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
"""
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])
inf = int(9e9)
distance = [inf] * n


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            if distance[next[0]] <= dist + next[1]:
                continue
            distance[next[0]] = dist + next[1]
            heapq.heappush(pq, (dist + next[1], next[0]))


dijkstra(0)
print(distance)