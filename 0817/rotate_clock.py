K = int(input())
clock = [12, 9, 6, 3]
K %= 360
K //= 90
for _ in range(K):
    clock.append(clock.pop(0))
for i in [0, 1, 3, 2]:
    print(clock[i], end=' ')
