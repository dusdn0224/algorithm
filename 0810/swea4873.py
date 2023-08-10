T = int(input())
for tc in range(1, T+1):
    string = input()
    # stack = [0] * len(string)
    stack = []
    top = -1
    for char in string:
        top += 1
        # if stack[top-1] == char:
        #     stack[top-1] = 0
        #     top -= 2
        # else:
        #     stack[top] = char
        if stack:
            if stack[top-1] == char:
                stack.pop()
                top -= 2
            else:
                stack.append(char)
        else:
            stack.append(char)
    # cnt = 0
    # for c in stack:
    #     if c != 0:
    #         cnt += 1
    # print(f'#{tc}', cnt)
    print(f'#{tc}', len(stack))
