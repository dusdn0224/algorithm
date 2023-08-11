T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    profit = 0
    max_price = arr[-1]
    for i in range(N - 2, -1, -1):
        if max_price < arr[i]:
            max_price = arr[i]
        else:
            profit += max_price - arr[i]

    # arr2 = arr[:]
    # buy_list = []
    # profit = 0
    # for price in arr2:
    #     if price != max(arr):
    #         buy_list.append(price)
    #     else:
    #         for item in buy_list:
    #             profit += (price - item)
    #             arr.remove(item)
    #         arr.remove(price)
    #         buy_list.clear()

    # arr2 = arr[:]
    # profit = 0
    # for price in arr2:
    #     profit += max(arr) - price
    #     arr.remove(price)

    print(f'#{tc}', profit)
