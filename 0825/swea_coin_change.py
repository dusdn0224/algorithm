T, n = map(int, input().split())
coin = list(map(int, input().split()))
dp = [0] * (T+1)
dp[0] = T + 1
for c in coin:
    dp[c] = 1
for i in range(min(coin) + 1, T+1):
    if not dp[i]:
        dp[i] = T + 1
        for j in range(n):
            dp[i] = min(dp[i - coin[j] if i - coin[j] >= min(coin) else 0], dp[i])
        dp[i] += 1
print(dp[T])
