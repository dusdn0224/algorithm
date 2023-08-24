def Bbit(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output, end=' ')
a = 0x10
x = 0x01020304
print('%d = ' % a, end='')
Bbit(a)
print()
print('0%X = ' % x, end='')
for i in range(0, 4):
    Bbit((x >> i * 8) & 0xff)
print(0xff00)
