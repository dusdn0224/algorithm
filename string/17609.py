T = int(input())


def pal(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return 2
    return 0


def psdpal(s):
    check = 0
    for char in s:
        cnt = s.count(char)
        if cnt % 2:
            check += 1


for _ in range(T):
    string = input()
    # print(pal(string))
    cnt1 = cnt2 = cnt3 = 0
    for i in range(len(string) // 2):
        if string[i] == string[len(string) - 1 - i]:
            cnt1 += 1
    # print(f'[{len(string) // 2}]', cnt1, cnt2, cnt3, sep=', ')
    print(string.replace('b', ''))
