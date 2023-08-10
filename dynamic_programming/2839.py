N = int(input())
min_bag = N // 3
check = 0
for n in range((N // 5) + 1):
    for m in range((N // 3) + 1):
        if 5 * n + 3 * m == N:
            check += 1
            if min_bag > n + m:
                min_bag = n + m
if check == 0:
    print(-1)
else:
    print(min_bag)

# a = int(input())
# n = a // 5
# result = -1
# for i in range(n, -1, -1):
#     temp = a - i * 5
#     if temp % 3 == 0:
#         result = i + temp // 3
#         break
# print(result)
