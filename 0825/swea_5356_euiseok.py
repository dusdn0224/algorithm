T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    print(f'#{tc} ', end='')
    for i in range(15):
        for k in range(5):
            try:
                print(arr[k][i], end='')
            except:
                continue
    print()
