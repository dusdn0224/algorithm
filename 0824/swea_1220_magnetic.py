T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        stack = []
        for j in range(N):
            if arr[j][i] == 1:
                stack.append(1)
            elif arr[j][i] == 2:
                if stack and stack[-1] == 1:
                    cnt += 1
                stack.append(2)
    print(f'#{tc}', cnt)
