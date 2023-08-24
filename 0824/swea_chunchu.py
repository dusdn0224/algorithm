N = int(input())
population = list(map(int, input().split()))
arr = [[0] * N for _ in range(N)]


def bfs(n):
    visited = [0] * N
    q = [n]
    popul = population[n]
    alli = []
    visited[n] = 1
    while q:
        t = q.pop(0)
        alli.append(t)
        for i in range(N):
            if arr[t][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
                popul += population[i]
    return popul, alli


T = int(input())
for _ in range(T):
    S, A, B = input().split()
    if S == 'alliance':
        arr[ord(A) - 65][ord(B) - 65] = 1
        arr[ord(B) - 65][ord(A) - 65] = 1
    else:
        p1, alli1 = bfs(ord(A) - 65)
        p2, alli2 = bfs(ord(B) - 65)
        if p1 > p2:
            for nation in alli2:
                population[nation] = 0
        elif p1 < p2:
            for nation in alli1:
                population[nation] = 0
        else:
            for nation in alli1:
                population[nation] = 0
            for nation in alli2:
                population[nation] = 0
cnt = 0
for i in population:
    if i:
        cnt += 1
print(cnt)
