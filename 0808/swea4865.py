T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    max_cnt = 0
    for char1 in str1:
        cnt = 0
        for char2 in str2:
            if char1 == char2:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc}', max_cnt)
