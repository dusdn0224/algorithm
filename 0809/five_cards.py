arr = list(input())
num = []  # [0, 0, 0, 0]으로 바꿔야할듯...
cnt = 0


def card(k):
    global num
    global cnt
    if k == 4:
        check = 0
        for i in range(3):
            if -3 <= int(num[i]) - int(num[i + 1]) <= 3:
                check += 1
        if check == 3:
            cnt += 1
        num.pop()  # num[3]만 계속 날아감
        return
    for i in arr:
        num.append(i)
        card(k + 1)


card(0)
print(cnt)


# card = list(input())
# path = [0] * 4
# cnt = 0
#
#
# def card_cnt(level):  # level은 현재 뽑은 카드의 수
#     global cnt
#     # 4장의 카드를 뽑았으면 경우의 수 증가
#     if level == 4:
#         cnt += 1
#         return  # 재귀호출 종료
#     for i in range(5):  # 5개의 카드 중 하나 선택
#         path[level] = card[i]  # 현재 레벨 경로에 선택한 카드를 저장
#         if int(path[level]) - int(path[level - 1]) >= 4:
#             continue
#         if int(path[level - 1]) - int(path[level]) >= 4:
#             continue
#         # 다음 레벨로 재귀 호출
#         card_cnt(level + 1)
#
#
# card_cnt(0)  # 시작 레벨은 0
# print(cnt)
