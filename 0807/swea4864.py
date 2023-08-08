T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    ans = 0
    if str1 in str2:
        ans = 1
    print(f'#{tc}', ans)

    # i = 0
    # j = 0
    # while j < len(str1) and i < len(str2):
    #     if str2[i] != str1[j]:
    #         i -= j
    #         j = -1
    #     i += 1
    #     j += 1
    # if j == len(str1):
    #     print(f'#{tc}', 1)
    # else:
    #     print(f'#{tc}', 0)
