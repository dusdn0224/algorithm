T = int(input())


def pal(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return 2
    else:
        return 0


def psdpal1(s):
    s = list(s)
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            s.pop(i)
            break
    for j in range(len(s) // 2):
        if s[j] != s[len(s) - 1 - j]:
            return 2
    else:
        return 1


def psdpal2(s):
    s = list(s)
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            s.pop(len(s) - 1 - i)
            break
    for j in range(len(s) // 2):
        if s[j] != s[len(s) - 1 - j]:
            return 2
    else:
        return 1


for _ in range(T):
    string = input()
    ans = pal(string)
    if ans == 2:
        ans = psdpal1(string)
    if ans == 2:
        ans = psdpal2(string)
    print(ans)
