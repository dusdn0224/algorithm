T = int(input())
arr = [int(input()) for _ in range(T)]
largest = max(arr)
dp = [0] * (largest + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, largest + 1):
    dp[i] = dp[i-1]
for j in arr:
    print(dp[j])