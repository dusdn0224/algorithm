T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_sum = 0
    min_sum = 1000000
    for i in range(N - M + 1):
        case_sum = 0
        for j in range(M):
            case_sum += arr[i + j]
        if case_sum > max_sum:
            max_sum = case_sum
        if case_sum < min_sum:
            min_sum = case_sum

    print(f'#{tc}', max_sum - min_sum)
