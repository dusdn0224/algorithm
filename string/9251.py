str1 = input()
str2 = input()
max_len = 0
for i in range(1 << len(str1)):
    for j in range(len(str1)):
        if i & (1 << j):
            print(str1[j], end=', ')
    print()
print()
