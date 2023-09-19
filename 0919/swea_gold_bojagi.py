import heapq
N = int(input())
W = list(map(int, input().split()))
for i in range(N):
    W[i] = [W[i], 0]
heapq.heapify(W)
cnt = 0
while True:
    a1 = heapq.heappop(W)
    if a1[1]:
        break
    else:
        cnt += 1
    a2 = heapq.heappop(W)
    if a2[1]:
        break
    else:
        cnt += 1
        heapq.heappush(W, [a2[0] * 2, 1])
print(cnt)