N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    m1, m2 = map(int, input().split())
    arr[m1].append(m2)
    arr[m2].append(m1)
coco = int(input())
q = [coco]
visited = [0] * (N+1)
visited[coco] = 1
while q:
    t = q.pop(0)
    for i in arr[t]:
        if not visited[i]:
            q.append(i)
            visited[i] = visited[t] + 1
cnt = 0
for n in visited:
    if 2 <= n <= 3:
        cnt += 1
print(cnt)
