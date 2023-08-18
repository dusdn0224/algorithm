N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
house_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            queue = list()
            queue.append((i, j))
            visited[i][j] = 1
            house = 1
            while queue:
                y, x = queue.pop(0)
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N:
                        if arr[ny][nx] and not visited[ny][nx]:
                            queue.append((ny, nx))
                            visited[ny][nx] = 1
                            house += 1
            cnt += 1
            house_lst.append(house)
print(cnt)
house_lst.sort()
for i in range(cnt):
    print(house_lst[i])
