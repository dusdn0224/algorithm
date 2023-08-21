T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    for i in sample:
        if passcode and i == passcode[0]:
            passcode.pop(0)
    if passcode:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', 1)

