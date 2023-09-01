A, B = map(int, input().split())
cnt = 0
while True:
    if B == A:
        break
    if not B % 2:
        cnt += 1
        B //= 2
    elif B % 10 == 1:
        cnt += 1
        B //= 10
    else:
        cnt = -1
        break
print(cnt)
