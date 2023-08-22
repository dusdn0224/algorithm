T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)
    for i in range(N):
        tree[i + 1] = arr[i]
        i += 1
        while i // 2 > 0:
            if tree[i] < tree[i // 2]:
                tree[i], tree[i // 2] = tree[i // 2], tree[i]
                i //= 2
            else:
                break
    ans = 0
    while N > 0:
        N //= 2
        ans += tree[N]
    print(f'#{tc}', ans)
