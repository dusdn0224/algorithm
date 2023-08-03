# # 버블정렬: 인접한 두 요소를 비교하여 큰 값을 오른쪽으로 이동시키는 과정을 반복
# numbers = [63, 31, 27, 11, 25]
#
#
# def bubble(arr):
#     for j in range(len(arr)):
#         for i in range(len(arr) - j - 1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#
#
# bubble(numbers)
# print(numbers)

# # 카운팅 정렬: 정수를 정렬하는 알고리즘, 각 숫자의 개수를 세어서 정렬
#
#
# def counting(arr):
#     max_value = max(arr)
#     # 카운트 저장할 리스트
#     count_arr = [0] * (max_value + 1)
#
#     for num in arr:
#         count_arr[num] += 1
#
#     sorted_arr = []
#     for i, count in enumerate(count_arr):  # 인덱스와 값을 쌍으로 반환
#         sorted_arr.extend([i] * count)  # iterable 추가
#
#     return sorted_arr
#
#
# list1 = [1, 4, 1, 2, 7, 5, 2]
# sorted_list = counting(list1)
# print(sorted_list)

# # 순열: 주어진 항목들로 만들 수 있는 모든 가능한 순서(튜플)
# # itertools 모듈 사용
# import itertools
# arr = [1, 2, 3]
# result = list(itertools.permutations(arr))
# print(result)

# # 탐욕 알고리즘: 각 단계에서 가장 최선의 선택을 하는 방법
# # 거스름돈을 줄 때 가장 적은 수의 동전을 사용하여 거스름돈을 주는 문제
# # 최선의 선택: 가장 큰 단위의 동전부터 사용하는 것
# # 실습: 동전 종류가 100원, 50원 10원 거스름돈이 380원이라면
# # 어떻게 해야 가장 적은 수의 동전으로 거스름돈을 받을 수 있을까요?
#
#
# def coin(change):
#     coin_dict = {}
#     coins = [100, 50, 10]
#     for i in coins:
#         coin_dict.setdefault(i, change // i)
#         change %= i
#     return coin_dict
#
#
# print(coin(380))
#
#
# def greedy(money, coins):
#     coins.sort(reverse=True)
#     # 거스름돈의 개수를 저장할 딕셔너리
#     change = {c: 0 for c in coins}
#     for c in coins:
#         while money >= c:
#             money -= c
#             # 해당 동전의 개수를 1씩 증가
#             change[c] += 1
#     return change
#
#
# result = greedy(380, [100, 50, 10])
# print(result)
