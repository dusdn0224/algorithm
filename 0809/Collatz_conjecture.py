N = int(input())
cnt = 0


def cc(n):
    global cnt
    if n == 1:
        return cnt
    elif n % 2:
        cnt += 1
        return cc(n * 3 + 1)
    else:
        cnt += 1
        return cc(n / 2)


print(cc(N))
