T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input()

    card = [0] * 10
    for i in arr:
        card[int(i)] += 1

    max_idx = 0
    for i in range(1, 10):
        if card[i] >= card[max_idx]:
            max_idx = i

    print(f'#{tc}', max_idx, card[max_idx])
