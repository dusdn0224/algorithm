N = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_mix = 2000000001
start = 0
end = N - 1
while start < end:
    mix = arr[start] + arr[end]
    if min_mix > abs(mix):
        min_mix = abs(mix)
        ans = [arr[start], arr[end]]
    if mix > 0:
        end -= 1
    elif mix < 0:
        start += 1
    else:
        ans = [arr[start], arr[end]]
        break
print(*ans)
