# def fibo(n):
#     global cnt
#     cnt += 1
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# cnt = 0
# print(fibo(30), cnt)
#
#
# def fibo1(n):
#     global cnt1
#     global memo
#     cnt1 += 1
#     if n >= 2 and memo[n] == 0:
#         memo[n] = (fibo1(n-1) + fibo1(n-2))
#     return memo[n]
#
#
# cnt1 = 0
# N = 30
# memo = [0] * (N+1)
# memo[0] = 0
# memo[1] = 1
# print(fibo1(N), cnt1)
#
#
# def fibo2(n):
#     dp = [0] * (n+1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
#
#
# print(fibo2(30))


"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""


def dfs(n, V, adj_m):
    # stack 생성
    stack = []
    # visited 생성
    visited = [0] * (V+1)
    # 시작점 방문 표시
    visited[n] = 1
    # do[n]
    print(n)
    while True:
        # 현재 정점 n에 인접하고 미방문 w 찾기
        for w in range(1, V+1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                # push(n), v = w
                stack.append(n)
                n = w
                # do[w]
                print(n)
                # w 방문 표시
                visited[n] = 1
                break
        else:
            # 스택에 지나온 정점이 남아있으면
            if stack:
                n = stack.pop()  # pop()해서 다시 다른 w ㅊ찾기
            else:
                break


V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)
