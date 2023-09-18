N, M = map(int, input().split())
arr = []
for _ in range(N):
    n = int(input())
    arr.append(1 / n)
for i in range(1000000000):
    snack = 0
    for bar in arr:
        snack += int(bar * i)
    if snack >= M:
        break
print(i)