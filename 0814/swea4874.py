T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []
    ans = 'error'
    for i in range(len(arr)):
        if arr[i].isnumeric():
            stack.append(int(arr[i]))
        elif arr[i] == '.' and i == len(arr) - 1:
            if len(stack) == 1:
                ans = stack[0]
        else:
            if len(stack) >= 2:
                n2 = stack.pop()
                n1 = stack.pop()
                if arr[i] == '+':
                    stack.append(n1 + n2)
                elif arr[i] == '-':
                    stack.append(n1 - n2)
                elif arr[i] == '*':
                    stack.append(n1 * n2)
                elif arr[i] == '/':
                    stack.append(n1 / n2)
            else:
                break
    print(f'#{tc}', ans)
