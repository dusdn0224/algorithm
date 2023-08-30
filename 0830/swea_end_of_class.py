N, M = map(int, input().split())
prices = [list(map(int, input().split())) for _ in range(M)]
six = one = 1001
for price in prices:
    six = min(six, price[0], price[1] * 6)
    one = min(one, price[1])
print(min((six * (N // 6 + 1)), (six * (N // 6)) + (one * (N % 6))))
