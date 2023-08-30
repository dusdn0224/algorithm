N = int(input())
cards = [int(input()) for _ in range(N)]
cards.sort()
if N == 1:
    comp = cards[0]
else:
    comp = (cards[0] + cards[1]) * (N-1)
for i in range(2, N):
    comp += cards[i] * (N - i)
print(comp)
