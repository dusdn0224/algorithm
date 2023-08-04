for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    arr2 = list(input().split())
    commands = []
    for i in range(len(arr2)):
        if arr2[i] == 'I':
            c = ['I']
            for j in range(i + 1, i + int(arr2[i + 2]) + 3):
                c.append(int(arr2[j]))
            commands.append(c)
        elif arr2[i] == 'D':
            c = ['D']
            for j in range(i + 1, i + 3):
                c.append(int(arr2[j]))
            commands.append(c)
        elif arr2[i] == 'A':
            c = ['A']
            for j in range(i + 1, i + int(arr2[i + 1]) + 2):
                c.append(int(arr2[j]))
            commands.append(c)
    for command in commands:
        if command[0] == 'I':
            for s in command[len(command):2:-1]:
                arr.insert(command[1], s)
        elif command[0] == 'D':
            for i in range(command[2]):
                arr.pop(command[1])
        elif command[0] == 'A':
            arr.extend(command[2:])
    print(f'#{tc}', *arr[:10])
