for _ in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))
    m = 1
    while True:
        num = arr.pop(0)
        num -= m
        if num <= 0:
            num = 0
            arr.append(num)
            break
        else:
            arr.append(num)
        m += 1
        if m > 5:
            m = 1
    print(f'#{tc}', *arr)
