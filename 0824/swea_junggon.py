T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            danjo = True
            check = str(arr[i] * arr[j])
            for c in range(len(check) - 1):
                if check[c] > check[c + 1]:
                    danjo = False
                    break
            if danjo:
                result = max(int(check), result)
    if not result:
        result = -1
    print(f'#{tc}', result)
