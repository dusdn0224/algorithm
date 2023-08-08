N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

dict1 = {}
for i in arr1:
    dict1[i] = 1
for i in arr2:
    print(dict1.get(i, 0), end=' ')
