arr = input()
y, m, d = arr.split('.')

if len(m) == 2:
    if m == '1X' or m == 'XX':
        mc = 3
    else:
        mc = 1
else:
    if m == 'X':
        mc = 9
    else:
        mc = 1

if len(d) == 2:
    if d == 'XX':
        dc = 22
    elif d[1] == 'X':
        if d[0] == '1' or d[0] == '2':
            dc = 10
        else:
            dc = 2
    elif d[0] == 'X':
        if d[1] == '0' or d[1] == '1':
            dc = 3
        else:
            dc = 2
    else:
        dc = 1
else:
    if d == 'X':
        dc = 9
    else:
        dc = 1

print(mc * dc)

'''
2025.X.1X
'''