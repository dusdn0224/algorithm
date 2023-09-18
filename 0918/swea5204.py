from collections import deque


def merge(lst_l, lst_r):
    global cnt
    result = []
    if lst_l[-1] > lst_r[-1]:
        cnt += 1
    lst_l = deque(lst_l)
    lst_r = deque(lst_r)
    while len(lst_l) > 0 or len(lst_r) > 0:
        if len(lst_l) > 0 and len(lst_r) > 0:
            if lst_l[0] <= lst_r[0]:
                result.append(lst_l.popleft())
            else:
                result.append(lst_r.popleft())
        elif len(lst_l) > 0:
            result.append(lst_l.popleft())
        elif len(lst_r) > 0:
            result.append(lst_r.popleft())
    return result


def mergesort(lst):
    if len(lst) == 1:
        return lst
    left = mergesort(lst[:len(lst)//2])
    right = mergesort(lst[len(lst)//2:])
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = mergesort(arr)
    print(f'#{tc}', ans[N//2], cnt)
