T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    for i in range(N-M, 0, -1):
        tree[i] += tree[i * 2]
        if i * 2 + 1 <= N:
            tree[i] += tree[i * 2 + 1]
    print(f'#{tc}', tree[L])
