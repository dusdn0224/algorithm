# def find(node):
#     if node != root(node):
#         root[node] = find(root[node])
#     return root[node]
#
#
# def union(x, y):
#     root_x = find(x)
#     root_y = find(y)
#     if root_x == root_y:
#         return
#     if rank[root_x] > rank[root_y]:
#         root[root_y] = root_x
#     else:
#         root[root_x] = root_y
#         if rank[root_x] == rank[root_y]:
#             rank[root_y] += 1


N = int(input())
# rank = [0] * 26
# root = [i for i in range(26)]
# for _ in range(N):
#     a, b = input().split()
#     union(ord(a) - 65, ord(b) - 65)
# for i in range(26):
#     find(i)
# DAT = [0] * 26
# team = 0
# for i in range(26):
#     DAT[root[i]] += 1
# indi = 0
# for data in DAT:
#     if data > 1:
#         team += 1
#     elif data == 1:
#         indi += 1
# print(team)
# print(indi)

arr = [[0] * 26 for _ in range(26)]
visited = [0] * 26
team = 0
solo = 0
for _ in range(N):
    n1, n2 = input().split()
    arr[ord(n1) - 65][ord(n2) - 65] = arr[ord(n2) - 65][ord(n1) - 65] = 1
for i in range(26):
    for j in range(26):
        if arr[i][j] and not visited[i]:
            q = [i]
            while q:
                t = q.pop(0)
                visited[t] = 1
                for k in range(26):
                    if arr[t][k] and not visited[k]:
                        q.append(k)
            team += 1
for v in visited:
    if not v:
        solo += 1
print(team)
print(solo)
