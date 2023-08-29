N = int(input())

dp = [N] * (N + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, N + 1):
    for j in range(int(i ** (1/2)) + 1, 0, -1):
        check = dp[i - j ** 2]
        if dp[i] > check:
            dp[i] = check + 1

print(dp[N])
