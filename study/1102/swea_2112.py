

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    columns = [[] for _ in range(W)]
    for _ in range(D):
        row = list(map(int, input().split()))
        for i in range(W):
            columns[i].append(row[i])
    check = columns[0][:]
    check[0] = 100
    print(columns)