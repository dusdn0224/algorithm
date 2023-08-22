def bst(n):
    global node
    if n <= N:
        bst(n * 2)
        tree[n] = node
        node += 1
        bst(n * 2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    node = 1
    bst(1)
    print(f'#{tc}', tree[1], tree[N // 2])

