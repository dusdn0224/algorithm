n = int(input())
mario = list(map(int, input().split()))
mario.insert(0, 0)
dp = [0] * (n+1)
if n >= 2:
    dp[2] = mario[2]
if n >= 7:
    dp[7] = mario[7]
for i in range(3, n+1):
    dp[i] = max(dp[i-2 if i - 2 >= 0 else 0], dp[i-7 if i - 7 >= 0 else 0]) + mario[i]
if n > 7:
    print(max(dp[n - 7 + 1:]))
else:
    print(max(dp))
