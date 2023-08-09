arr = [3, 5, 1, 9, 7]
for _ in range(4):
    move = input()
    if move == 'R':
        for i in range(len(arr)-1, 0, -1):
            arr[i], arr[i-1] = arr[i-1], arr[i]
    elif move == 'L':
        for i in range(len(arr)-1):
            arr[i], arr[i-1] = arr[i-1], arr[i]
    print(arr)
