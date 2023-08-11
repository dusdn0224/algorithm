n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


# stack = []
# visited = [0] * n
# s = 0
# visited[s] = 1
# while True:
#     for i in range(n):
#         if arr[s][i] == 1 and visited[i] == 0:
#             stack.append(s)
#             s = i
#             visited[s] = 1
#             break
#     else:
#         if stack:
#             if len(stack) == 2:
#                 print(*stack, s)
#             s = stack.pop()
#         else:
#             break

stack = []


def dfs(now):
    global stack
    stack.append(now)
    for i in range(n):
        if arr[now][i] == 1:
            dfs(i)
    if len(stack) == 3:
        print(*stack)
    stack.pop()


dfs(0)
