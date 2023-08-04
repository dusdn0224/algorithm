for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    arr2 = list(input().split())
    commands = []
    for i in range(len(arr2)):
        if arr2[i] == 'I':
            c = []
            for j in range(i + 1, i + int(arr2[i + 2]) + 3):
                c.append(int(arr2[j]))
            commands.append(c)
    for command in commands:
        for s in command[len(command):1:-1]:
            arr.insert(command[0], s)
    print(f'#{tc}', *arr[:10])
