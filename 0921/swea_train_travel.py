import heapq
N, T = map(int, input().split())
connect = [[] for _ in range(N)]
for _ in range(T):
    a, b, w = map(int, input().split())
    connect[a].append([b, w])
costs = [9e9] * N
heap = []
heapq.heappush(heap, (0, 0))
costs[0] = 0
while heap:
    cost, now = heapq.heappop(heap)
    if costs[now] < cost:
        continue
    for next in connect[now]:
        if costs[next[0]] <= cost + next[1]:
            continue
        costs[next[0]] = cost + next[1]
        heapq.heappush(heap, (cost + next[1], next[0]))
if costs[N-1] == 9e9:
    print('impossible')
else:
    print(costs[N-1])
