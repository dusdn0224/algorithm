T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * (n + 1)
    dp[1:4] = [1, 2, 4]
    for i in range(4, n+1):
        for j in range(1, 4):
            dp[i] += dp[i - j]
    print(dp[n])
