n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
stack = []
visited = [0] * n
s = 0
visited[s] = 1
print(s, end=' ')
while True:
    for i in range(n):
        if arr[s][i] == 1 and visited[i] == 0:
            stack.append(s)
            s = i
            visited[s] = 1
            print(s, end=' ')
            break
    else:
        if stack:
            s = stack.pop()
        else:
            break


def dfs(now):
    print(now, end=' ')
    for i in range(n):
        if arr[now][i] == 1:
            dfs(i)


dfs(0)
