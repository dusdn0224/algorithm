string = input()
adj_m = [list(map(int, input().split())) for _ in range(len(string))]
n = 0
stack = []
visited = [0] * (len(string))
visited[n] = 1
print(string[n], end='')
while True:
    for i in range(1, len(string)):
        if adj_m[n][i] == 1 and visited[i] == 0:
            stack.append(n)
            n = i
            visited[n] = 1
            print(string[n], end='')
            break
    else:
        if stack:
            n = stack.pop()
        else:
            break
