T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for b in B:
        start = 0
        end = N - 1
        warigari = True
        find = False
        prev = 0  # 왼쪽은 1, 오른쪽은 2
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == b:
                find = True
                break
            elif A[mid] < b:
                start = mid + 1
                if prev == 2:
                    warigari = False
                    break
                else:
                    prev = 2
            else:
                end = mid - 1
                if prev == 1:
                    warigari = False
                    break
                else:
                    prev = 1
        if find and warigari:
            cnt += 1
    print(f'#{tc}', cnt)
