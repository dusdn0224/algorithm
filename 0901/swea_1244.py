# def change(cnt):
#     global max_n, ans
#     if cnt == int(c):
#         n = 0
#         for s in range(N):
#             n += int(number[s]) * (10 ** (N - (s + 1)))
#         if max_n < n:
#             max_n = n
#             ans = number[:]
#     else:
#         for i in range(N - 1):
#             for j in range(i + 1, N):
#                 number[i], number[j] = number[j], number[i]
#                 change(cnt+1)
#                 number[i], number[j] = number[j], number[i]


T = int(input())
for tc in range(1, T+1):
    number, c = input().split()
    # number = list(number)
    # N = len(number)
    # ans = number[:]
    # cnt = 0
    # max_n = 0
    # while cnt < int(c):
    #     number = ans[:]
    #     for i in range(N - 1):
    #         for j in range(i + 1, N):
    #             number[i], number[j] = number[j], number[i]
    #             n = 0
    #             for s in range(N):
    #                 n += int(number[s]) * (10 ** (N - (s+1)))
    #             if max_n < n:
    #                 max_n = n
    #                 ans = number[:]
    #             number[i], number[j] = number[j], number[i]
    #     cnt += 1
    # # max_n = 0
    # # change(0)
    # print(f'#{tc}', end=' ')
    # for m in ans:
    #     print(m, end='')
    # print()

    c = int(c)
    now = set([number])
    next = set()
    for _ in range(c):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(len(number) - 1):
                for j in range(i+1, len(number)):
                    s[i], s[j] = s[j], s[i]
                    next.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, next = next, now
    result = max(map(int, now))
    print(f'#{tc} {result}')
