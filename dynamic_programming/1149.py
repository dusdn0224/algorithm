N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]
dp[0] = arr[0]
for i in range(1, N):
    dp[i][0] = min(arr[i][0] + dp[i - 1][1], arr[i][0] + dp[i - 1][2])
    dp[i][1] = min(arr[i][1] + dp[i - 1][0], arr[i][1] + dp[i - 1][2])
    dp[i][2] = min(arr[i][2] + dp[i - 1][0], arr[i][2] + dp[i - 1][1])
ans = min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2])
print(ans)
