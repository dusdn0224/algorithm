Q = int(input())
K = list(map(int, input().split()))
# tree = [1]
# i = 0
# while len(tree) <= 5000:
#     if tree[i] * 2 not in tree:
#         tree.append(tree[i] * 2)
#         j = len(tree) - 1
#         while j > 0:
#             if tree[j] < tree[j-1]:
#                 tree[j], tree[j-1] = tree[j-1], tree[j]
#                 j -= 1
#             else:
#                 break
#     if tree[i] * 3 not in tree:
#         tree.append(tree[i] * 3)
#         j = len(tree) - 1
#         while j > 0:
#             if tree[j] < tree[j-1]:
#                 tree[j], tree[j-1] = tree[j-1], tree[j]
#                 j -= 1
#             else:
#                 break
#     if tree[i] * 5 not in tree:
#         tree.append(tree[i] * 5)
#         j = len(tree) - 1
#         while j > 0:
#             if tree[j] < tree[j-1]:
#                 tree[j], tree[j-1] = tree[j-1], tree[j]
#                 j -= 1
#             else:
#                 break
#     i += 1
# for n in K:
#     print(tree[n - 1], end=' ')

import heapq

tree = [1]
i = 0
while len(tree) <= 5000:
    if tree[i] * 2 not in tree:
        heapq.heappush(tree, tree[i] * 2)
    if tree[i] * 3 not in tree:
        heapq.heappush(tree, tree[i] * 3)
    if tree[i] * 5 not in tree:
        heapq.heappush(tree, tree[i] * 5)
    i += 1
    tree.sort()
for n in K:
    print(tree[n - 1], end=' ')
