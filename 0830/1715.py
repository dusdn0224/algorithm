import heapq

N = int(input())

# cards = [int(input()) for _ in range(N)]
# comp = 0
# for _ in range(N-1):
#     cards.sort(reverse=True)
#     a = cards.pop()
#     b = cards.pop()
#     comp += a + b
#     cards.append(a+b)
# print(comp)

cards = []
for _ in range(N):
    card = int(input())
    heapq.heappush(cards, card)
comp = 0
for i in range(N-1):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    comp += a + b
    heapq.heappush(cards, a + b)
print(comp)
