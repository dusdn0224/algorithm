# def f(i, N):
#     if i == N:
#         return
#     else:
#         B[i] = A[i]
#         f(i + 1, N)
#         return
#
#
# N = 10
# A = [i for i in range(1, N + 1)]
# B = [0] * N
# f(0, N)
# # print(B)
#
#
# def fb(i, N, s):
#     if i == N:
#         # print(bit, end='')
#         # s = 0
#         # for j in range(N):
#         #     if bit[j]:
#         #         s += A[j]
#         #         print(A[j], end=' ')
#         # print(f': {s}')
#         if s == 10:
#             print(bit, end=' ')
#             for j in range(N):
#                 if bit[j]:
#                     print(A[j], end=' ')
#             print()
#         return
#     else:
#         bit[i] = 1
#         fb(i + 1, N, s + A[i])
#         bit[i] = 0
#         fb(i + 1, N, s)
#         return
#
#
# bit = [0] * N
# fb(0, N, 0)


# def f(i, N):
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N):
#             A[i], A[j] = A[j], A[i]
#             f(i + 1, N)
#             A[i], A[j] = A[j], A[i]
#
#
# A = [1, 2, 3]
# f(0, 3)


def f1(b, e):
    if b == 0:
        return 1
    r = 1
    for i in range(e):
        r *= b
    return r


def f2(b, e):
    d = 1
    if b == 0 or e == 0:
        return 1
    if e % 2:
        r = f2(b, (e - 1) // 2)
        return r * r * b
    else:
        r = f2(b, e // 2)
        return r * r


print(f1(2, 10))
print(f2(2, 10))
