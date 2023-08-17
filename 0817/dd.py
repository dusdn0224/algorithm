# def enQ(data):
#     global rear
#     if rear == Qsize - 1:
#         print('Q is Full')
#     else:
#         rear += 1
#         Q[rear] = data
#         print(Q)
#
#
# def deQ():
#     global front
#     if front == Qsize - 1:
#         return 'Q is Empty'
#     else:
#         front += 1
#         return Q[front]
#
#
# Qsize = 3
# Q = [0] * Qsize
# rear = front = -1
#
# enQ(1)
# enQ(2)
# enQ(3)
# enQ(4)
#
# print(deQ())
# print(deQ())
# print(deQ())
# print(deQ())
#
#
# Q2 = []
#
# Q2.append(1)
# print(Q2)
# Q2.append(2)
# print(Q2)
# Q2.append(3)
# print(Q2)
#
# print(Q2.pop(0))
# print(Q2.pop(0))
# print(Q2.pop(0))


# def encQ(data):
#     global rear
#     if (rear + 1) % cQsize == front:
#         print('cQ is Full')
#     else:
#         rear = (rear + 1) % cQsize
#         cQ[rear] = data
#         print(cQ)
#
#
# def decQ():
#     global front
#     front = (front + 1) % cQsize
#     return cQ[front]
#
#
# cQsize = 4
# cQ = [0] * cQsize
# rear = front = 0
#
# encQ(1)
# encQ(2)
# encQ(3)
# print(decQ())
# print(decQ())
# encQ(4)


# from collections import deque
# q = deque()
# q.append(1)
# print(q)
# q.append(2)
# print(q)
# q.append(3)
# print(q)
# print(q.popleft())
# print(q)
# print(q.popleft())
# print(q)
# print(q.popleft())
# print(q)


