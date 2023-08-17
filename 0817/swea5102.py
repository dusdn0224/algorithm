T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        e1, e2 = map(int, input().split())
        arr[e1][e2] = arr[e2][e1] = 1
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    Q = []
    Q.append(S)
    while Q:
        t = Q.pop(0)
        for i in range(V + 1):
            if arr[t][i] and not visited[i]:
                Q.append(i)
                visited[i] = visited[t] + 1
    print(f'#{tc}', visited[G])
