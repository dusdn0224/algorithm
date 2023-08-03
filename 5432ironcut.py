T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    for i in range(len(arr)):
        if arr[i] == '(':
            if arr[i + 1] != ')':
                arr[i] = '['
        if arr[i] == ')':
            if arr[i - 1] != '(':
                arr[i] = ']'
    result = 0
    cnt = 0
    for bracket in arr:
        if bracket == '[':
            cnt += 1
        elif bracket == '(':
            result += cnt
        elif bracket == ']':
            result += 1
            cnt -= 1
    print(f'#{tc}', result)
