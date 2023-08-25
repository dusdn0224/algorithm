T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    wait = [0] * (max(arr) + 1)
    result = 'Possible'
    for i in range(N):
        if i + 1 > (arr[i] // M) * K:
            result = 'Impossible'
            break
    print(f'#{tc}', result)
