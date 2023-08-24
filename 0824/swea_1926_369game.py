N = int(input())
for i in range(1, N+1):
    cnt = 0
    for c in str(i):
        if c == '3' or c == '6' or c == '9':
            cnt += 1
    if cnt:
        print('-' * cnt, end=' ')
        continue
    print(i, end=' ')
