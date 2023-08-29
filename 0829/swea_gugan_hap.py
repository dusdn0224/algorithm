N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for i in range(N):
    hap = 0
    for n in A[i:]:
        hap += n
        if hap == M:
            cnt += 1
            break
print(cnt)
