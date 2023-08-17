def bfs(table, start):
    visited = [0] * 6
    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        t = queue.pop(0)
        visited[t] = 1
        print(t, end=' ')
        for i in range(len(table[t])):
            if table[t][i] and not visited[i]:
                queue.append(i)


arr = [[0] * 6 for _ in range(6)]
arr[0][1] = arr[0][4] = arr[1][2] = arr[1][5] = arr[2][3] = 1

K = int(input())
bfs(arr, K)
