N = int(input())


def binary(n):
    # num_bin = ''
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        # num_bin += binary(n // 2) + f'{n % 2}'
        # return num_bin
        return binary(n // 2) + str(n % 2)


print(binary(N))
