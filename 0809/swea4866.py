T = int(input())
for tc in range(1, T+1):
    arr = input()
    stack = [0] * len(arr)
    top = -1
    result = 1
    for char in arr:
        if char == '(' or char == '{':
            top += 1
            stack[top] = char
        elif char == ')':
            if top == -1:
                result = 0
            elif stack[top] != '(':
                result = 0
            stack[top] = 0
            top -= 1
        elif char == '}':
            if top == -1:
                result = 0
            elif stack[top] != '{':
                result = 0
            stack[top] = 0
            top -= 1
    # if ('(' or '{') in stack:
    #     result = 0
    if top != -1:
        result = 0
    print(f'#{tc}', result)
