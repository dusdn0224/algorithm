def solution(money):
    N = len(money)
    dp = [0] * N
    dp[:2] = money[:2]
    for k in range(2, N):
        dp[k] = max(dp[k-2] + money[k], dp[k-1])
    return dp