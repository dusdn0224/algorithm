import heapq
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
heap = []
distance = [[9e9] * M for _ in range(N)]
heapq.heappush(heap, (arr[0][0], 0, 0))
distance[0][0] = arr[0][0]
while heap:
    dist, y, x = heapq.heappop(heap)
    if distance[y][x] < dist:
        continue
    for ny, nx in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
        if 0 <= ny < N and 0 <= nx < M:
            if distance[ny][nx] <= dist + arr[ny][nx]:
                continue
            distance[ny][nx] = dist + arr[ny][nx]
            heapq.heappush(heap, (dist + arr[ny][nx], ny, nx))
print(distance[N-1][M-1])
