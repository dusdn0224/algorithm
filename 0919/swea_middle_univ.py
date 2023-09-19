import heapq
N = int(input())
left = []
right = []
now = 500
for i in range(1, N+1):
    p1, p2 = map(int, input().split())
    if p1 > now:
        heapq.heappush(right, p1)
    else:
        heapq.heappush(left, -p1)
    if p2 > now:
        heapq.heappush(right, p2)
    else:
        heapq.heappush(left, -p2)
    if len(left) > len(right):
        heapq.heappush(right, now)
        now = -heapq.heappop(left)
        print(now)
    elif len(left) < len(right):
        heapq.heappush(left, -now)
        now = heapq.heappop(right)
        print(now)
    else:
        print(now)