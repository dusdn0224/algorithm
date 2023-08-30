N, K = map(int, input().split())
cnt = 0
coins = [int(input()) for _ in range(N)]
for coin in coins[::-1]:
    cnt += K // coin
    K %= coin
print(cnt)
