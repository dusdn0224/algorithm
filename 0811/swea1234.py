for tc in range(1, 11):
    N, string = input().split()
    stack = []
    for i in range(int(N)):
        if stack and stack[-1] == string[i]:
            stack.pop()
        else:
            stack.append(string[i])
    print(f'#{tc}', ''.join(stack))
