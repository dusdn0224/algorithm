T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    count = 0
    max_count = 0
    for i in arr:
        if i == 0:
            count = 0
        elif i == 1:
            count += 1
        if max_count < count:
            max_count = count

    print(f'#{tc}', max_count)
