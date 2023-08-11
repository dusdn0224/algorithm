n = int(input())
evid = [-1, 0, 0, 1, 2, 4, 4]
timestamp = [8, 3, 5, 6, 8, 9, 10]
stack = []


def dfs(s):
    global stack
    stack.append(s)
    if evid[s] == -1:
        print(f'{s}번 index(출발)')
        return
    dfs(evid[s])
    print(f'{s}번 index({timestamp[s]}시)')


dfs(n)
# for i in stack[::-1]:
#     if evid[i] == -1:
#         print(f'{i}번 index(출발)')
#     else:
#         print(f'{i}번 index({timestamp[i]}시)')
