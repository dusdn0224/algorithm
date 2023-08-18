N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    m1, m2 = map(int, input().split())
    arr[m1][m2] = arr[m2][m1] = 1
R, K = map(int, input().split())

# visited = [0] * (N + 1)
# Q = []
# Q.append(R)  # 시작점 넣기
# visited[R] = 1  # 시작점 방문표시
#
# while Q:
#     t = Q.pop(0)  # dequeue
#     for i in range(N + 1):  # N까지
#         if arr[t][i] and not visited[i]:  # 연결되어있고 방문하지 않았다면
#             Q.append(i)  # enqueue
#             visited[i] = visited[t] + 1  # 거리 재기
#
# cnt = 0  # 후보 지역 개수
# for i in range(1, N + 1):  # 1부터 N까지
#     if visited[i] - 1 <= K:  # 시작점의 방문 거리가 1이었으므로 1 빼주기
#         cnt += 1  # 개수 + 1
#
# print(cnt)


visited = [False] * (N + 1)
Q = [(R, 0)]
visited[R] = True
cnt = 0

while Q:
    print(Q)
    t, d = Q.pop(0)
    if d <= K:
        cnt += 1
    for i in range(N + 1):
        if arr[t][i] and not visited[i]:
            visited[i] = True
            Q.append((i, d+1))
print(cnt)
