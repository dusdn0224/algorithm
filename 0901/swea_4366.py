T = int(input())
for tc in range(1, T+1):
    two = input()
    three = list(map(int, input()))
    N = len(two)
    M = len(three)
    ans = 0
    binary = int(two, 2)
    bin_list = [0] * N
    for i in range(N):
        bin_list[i] = binary ^ (1 << i)
    for j in range(M):
        num1 = 0
        num2 = 0
        for k in range(M):
            if j != k:
                num1 = num1 * 3 + three[k]
                num2 = num2 * 3 + three[k]
            else:
                num1 = num1 * 3 + (three[k] + 1) % 3
                num2 = num2 * 3 + (three[k] + 2) % 3
        if num1 in bin_list:
            ans = num1
            break
        if num2 in bin_list:
            ans = num2
            break
    print(f'#{tc}', ans)
