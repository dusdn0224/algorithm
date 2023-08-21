"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
def preorder(n):
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])


V = int(input())  # 정점 수 = 마지막 정점 번호
E = V - 1         # tree의 간선 수 = 정점 수 - 1
arr = list(map(int, input().split()))
# 부모를 인덱스로 자식을 저장
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
par = [0] * (V+1)
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p
# print(ch1)
# print(ch2)
# print(par)
# preorder(1)
root = 1
while par[root] != 0:
    root += 1
preorder(root)
