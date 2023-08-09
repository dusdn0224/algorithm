# def push(item, size):
#     global top
#     top += 1
#     if top == size:
#         print('overflow')
#     else:
#         stack[top] = item
#
#
# size = 10
# stack = [0] * size
# top = -1
#
# push(10, size)
# top += 1
# stack[top] = 20
#
# print(stack)

def fibo1(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = (fibo1(n-1) + fibo1(n-2))
    return memo[n]
n = 9
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibo1(n))
