def bfs(table, start):
    visited = [0] * 6
    queue = []
    queue.append(start)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
            print(t)
            for i in range(len(table[t])):
                if table[t][i] and not visited[i]:
                    queue.append(i)


arr = [[0] * 6 for _ in range(6)]
arr[0][4] = arr[1][0] = arr[1][2] = arr[1][5] = arr[2][0] = 1
arr[2][3] = arr[3][0] = arr[3][1] = arr[4][1] = arr[4][3] = 1
arr[4][5] = arr[5][2] = arr[5][3] = 1

K = int(input())
bfs(arr, K)
