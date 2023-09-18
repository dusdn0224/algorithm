def partition(lst, l, r):
    p = lst[l]
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= p:
            i += 1
        while i <= j and lst[j] >= p:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j


def quicksort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quicksort(lst, l, s - 1)
        quicksort(lst, s + 1, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, N-1)
    print(f'#{tc}', arr[N//2])
