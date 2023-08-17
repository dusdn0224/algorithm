N = 20  # 마이쮸 개수
mc = [0] * (N + 1)  # 개인이 가진 마이쮸 개수
Q = []  # Queue

p = 1  # 1번부터 시작
while True:
    if Q:
        r = Q.pop(0)  # 제일 앞에 있는 사람
        Q.append(r)  # 맨 뒤에 넣기
        mc[r] += 1  # 마이쮸 하나 주기
        N -= 1  # 전체 개수 하나 빼기
        if N == 0:  # 마이쮸 다 줌
            print(r)  # 마지막 마이쮸 가져간 사람
            break
    Q.append(p)  # 새로 들어오는 사람 맨 뒤에 넣기
    mc[p] += 1  # 마이쮸 하나 주기
    N -= 1  # 전체 개수 하나 빼기
    if N == 0:  # 마이쮸 다 줌
        print(p)  # 마지막 마이쮸 가져간 사람
        break
    p += 1  # 다음에 새로 들어오는 사람은 번호 + 1

print(mc)
print(Q)
