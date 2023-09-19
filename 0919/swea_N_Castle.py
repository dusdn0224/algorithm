def f(cnt, lst):
    global ans
    if cnt == N:
        ans += 1
        return
    for i in range(N):
        if i not in lst:
            lst.append(i)
            f(cnt+1, lst)
            lst.pop()


N = int(input())
ans = 0
f(0, [])
print(ans)