'''
AB100CDEF112F4G5
'''

sentence = input()
name = ''
number = ''
for i in range(len(sentence)):
    if ord(sentence[i]) >= ord('A'):
        name += sentence[i]
        if 0 <= i - 1 and ord(sentence[i - 1]) < ord('A'):
            print(f'#{int(number) + 17}')
            number = ''
    else:
        number += sentence[i]
        if 0 <= i - 1 and ord(sentence[i - 1]) >= ord('A'):
            print(f'{name}', end='')
            name = ''
        if i == len(sentence) - 1:
            print(f'#{int(number) + 17}')
