M = int(input())
cnt = 0
for coin in [500, 100, 50, 10]:
    cnt += M // coin
    M %= coin
print(cnt)
