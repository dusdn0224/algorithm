expression = input().split('-')
result = 0
for i in range(len(expression)):
    num = 0
    plus = expression[i].split('+')
    for n in plus:
        num += int(n)
    if i == 0:
        result += num
    else:
        result -= num
print(result)
