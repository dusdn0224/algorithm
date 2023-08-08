for T in range(10):
    tc = input()
    find = input()
    sentence = input()
    i = 0
    j = 0
    cnt = 0
    while i < len(sentence):
        if sentence[i] != find[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == len(find):
            cnt += 1
            j = 0
    print(f'#{tc}', cnt)
