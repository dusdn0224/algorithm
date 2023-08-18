m, n = map(int, input().split())
k = int(input())
arr = [[0] * (m+1) for _ in range(n+1)]
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(y1, y2), max(y1, y2) + 1):
        for j in range(min(x1, x2), max(x1, x2) + 1):
            pass
            # arr[i][j][0].append(b)
            arr[i][j] += 1
sx, sy, dx, dy = map(int, input().split())
# for i in range(n+1):
#     print(arr[i])
visited = [[0] * (m+1) for _ in range(n+1)]
q = [(sy, sx, 1, 0)]
visited[sy][sx] = 1
while q:
    i, j, b, d = q.pop(0)
    if (i, j) == (dy, dx):
        break
    for di, dj, direc in [(-1, 0, 0), (1, 0, 0), (0, -1, 1), (0, 1, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n+1 and 0 <= nj < m+1:
            if arr[ni][nj] and not visited[ni][nj]:
                if (i, j) == (sy, sx) or d == direc:
                    q.append((ni, nj, b, direc))
                else:
                    q.append((ni, nj, b+1, direc))
                visited[ni][nj] = 1
print(b)

'''
for i in range(n+1):
    print(arr[i])
'''