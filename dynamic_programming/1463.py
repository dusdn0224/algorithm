N = int(input())
# cnt = 0
# while N != 1:
#     cnt += 1
#     if N % 3 != 0 and N % 2 != 0:
#         N -= 1
#     pass

dp = [0] * (N + 1)
dp[2:6] = [1, 1, 2, 3]
for i in range(6, N + 1):
    if i % 3 != 0 and i % 2 == 0:
        cnt = min(dp[i // 2] + 1, dp[i - 1] + 1)
    elif i % 3 == 0 and i % 2 != 0:
        cnt = min(dp[i // 3] + 1, dp[i - 1] + 1)
    elif i % 3 == 0 and i % 2 == 0:
        first = min(dp[i // 2] + 1, dp[i // 3] + 1)
        cnt = min(first, dp[i - 1] + 1)
    else:
        cnt = dp[i - 1] + 1
    dp[i] = cnt
print(dp[N])
