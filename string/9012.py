T = int(input())
for _ in range(T):
    arr = input()
    stack = [0] * len(arr)
    top = -1
    result = 'YES'
    for char in arr:
        if char == '(':
            top += 1
            stack[top] = char
        elif char == ')':
            if top == -1:
                result = 'NO'
            elif stack[top] != '(':
                result = 'NO'
            stack[top] = 0
            top -= 1
    if top != -1:
        result = 'NO'
    print(result)
