S = int(input())
D = int(input())
visited = [0] * 100001
queue = [S]
while queue:
    t = queue.pop(0)
    if t == D:
        break
    c = [t // 2, t * 2, t + 1, t - 1]
    for i in c:
        if 0 <= i <= 100000 and not visited[i]:
            queue.append(i)
            visited[i] = visited[t] + 1
print(visited[D])
