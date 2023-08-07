T = int(input())


def is_subset(sample, bit):
    subset = [sample[i] for i in range(len(sample)) if bit & (1 << i)]
    return subset


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    Sample = list(map(int, input().split()))
    PassCode = list(map(int, input().split()))

    passcode_str = ''.join(map(str, PassCode))
    found = False

    for i in range(1 << N):
        subset = is_subset(Sample, i)
        constructed_str = ''.join(map(str, subset))

        if constructed_str == passcode_str:
            found = True
            break

    if found:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
