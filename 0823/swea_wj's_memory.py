T = int(input())
for tc in range(1, T+1):
    memory = input()
    cnt = 0
    if memory[0] == '1':
        cnt += 1
    for i in range(1, len(memory)):
        if memory[i] != memory[i - 1]:
            cnt += 1
    print(f'#{tc}', cnt)
