N = int(input())
T = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(T):
    t1, t2 = map(int, input().split())
    arr[t1][t2] = arr[t2][t1] = 1
coco = int(input())
spouse = int(input())
visited = [0] * (N + 1)
Q = []
Q.append(coco)
while Q:
    t = Q.pop(0)
    visited[t] = 1
    for i in range(N + 1):
        if arr[t][i] and not visited[i]:
            Q.append(i)
if visited[spouse]:
    print('YES')
else:
    print('NO')
