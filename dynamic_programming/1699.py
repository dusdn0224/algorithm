N = int(input())

cnt = 0
while N > 0:
    N -= (int(N ** (1 / 2))) ** 2
    cnt += 1
print(cnt)

dp = [0] * 100001
dp[1] = 1
for i in range(2, 100001):
    for j in range(1, int((i ** (1/2)))):
        # dp[i] =
        pass
