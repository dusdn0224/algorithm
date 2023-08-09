N = int(input())


def hap(n):
    if n < 10:
        return n
    else:
        return (n % 10) + hap(n // 10)


print(hap(N))
