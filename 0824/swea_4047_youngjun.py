T = int(input())
for tc in range(1, T+1):
    arr = input()
    cards = []
    SDHC = [13] * 4
    error = False
    for card in range(0, len(arr), 3):
        card = arr[card: card + 3]
        if card in cards:
            error = True
            break
        else:
            cards.append(card)
        if card[0] == 'S':
            SDHC[0] -= 1
        elif card[0] == 'D':
            SDHC[1] -= 1
        elif card[0] == 'H':
            SDHC[2] -= 1
        elif card[0] == 'C':
            SDHC[3] -= 1
    if error:
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc}', *SDHC)
