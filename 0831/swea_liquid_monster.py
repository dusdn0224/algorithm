N = int(input())
liquid = list(map(int, input().split()))
time = 0
for _ in range(N-1):
    liquid.sort(reverse=True)
    a = liquid.pop()
    b = liquid.pop()
    time += a + b
    liquid.append(a + b)
print(time)
