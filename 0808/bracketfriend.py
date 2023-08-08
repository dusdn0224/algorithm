arr = input()
ans = 0
for i in range(len(arr)):
    if arr[i] == '[':
        # j = i + 1
        # num = ''
        # while arr[j] != ']':
        #     num += arr[j]
        #     j += 1
        # ans += int(num)
        ans += int(arr[i+1:arr.find(']', i)])
    elif arr[i] == '{':
        # j = i + 1
        # num = ''
        # while arr[j] != '}':
        #     num += arr[j]
        #     j += 1
        # ans *= int(num)
        ans *= int(arr[i+1:arr.find('}', i)])
print(ans)

'''
ABC123[10]B{3}AT[20][10]BB{2}Q
'''
