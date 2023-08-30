def cart(i, battery):
    global min_battery
    if i == N:
        battery += arr[route[-2]][route[-1]]
        min_battery = min(min_battery, battery)
    elif min_battery <= battery:
        return
    else:
        for j in range(i, N):
            route[i], route[j] = route[j], route[i]
            cart(i+1, battery + arr[route[i-1]][route[i]])
            route[i], route[j] = route[j], route[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_battery = 100 ** 2
    route = [i for i in range(N)]
    route.append(0)
    cart(1, 0)
    print(f'#{tc}', min_battery)
