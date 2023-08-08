arr = input()
num = ''
result = 0
for i in range(len(arr)-1, -1, -1):
    if ord(arr[i]) >= ord('0'):
        num = arr[i] + num
        if i == 0:
            result += int(num)
    elif arr[i] == '+':
        result += int(num)
        num = ''
    elif arr[i] == '-':
        result -= int(num)
        num = ''
print(result)

'''
100+100-50+30
'''

# ex = input()
# if ex[0] == '-':
#     ex = '0' + ex
# word = ex.split('+')
# ans = 0
# for w in word:
#     w = w.split('-')
#     inner_ans = int(w[0])
#     for i in range(1, len(w)):
#         inner_ans -= int(w[i])
#     ans += inner_ans
# print(ans)
