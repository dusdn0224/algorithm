N, M = map(int, input().split())
arr = list(map(int, input().split()))

# min_cut = M + 1
# h = 0
# while min_cut > M:
#     cut = 0
#     for i in arr:
#         if i > h:
#             cut += i - h
#     if min_cut > cut:
#         min_cut = cut
#     h += 1
# print(h - 1)

start = 0
end = max(arr)
ans = 0
while start <= end:
    cut = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            cut += i - mid

    if cut == M:
        break
    elif cut < M:
        end = mid - 1
        mid -= 1
    else:
        start = mid + 1

    if cut < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(mid)
print(ans)
