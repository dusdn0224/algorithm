Q = int(input())  # 명령의 수
rabbits = []  # 토끼 리스트
first = list(map(int, input().split()))  # 첫번째 명령
N, M, P = first[1:4]  # N x M 격자, P마리 토끼

for i in range(4, 3 + 2 * P, 2):
    pid, d = first[i:i + 2]  # 각 토끼의 pid(고유번호), d(이동거리)
    # [총 점프 횟수, 행 + 열, 행, 열, 고유번호, 이동거리, 점수]
    rabbits.append([0, 2, 1, 1, pid, d, 0])

for _ in range(Q - 2):  # 첫번째와 마지막 명령을 뺀 나머지 명령들
    play = list(map(int, input().split()))
    if play[0] == 200:  # 경주 진행
        picked = set()  # 뽑힌 토끼 리스트
        for _ in range(play[1]):
            rabbits.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
            jump, now, q, p, pid_now, d_now, point = rabbits[0]  # 최고 우선순위 토끼
            picked.add(pid_now)
            # 이동할 거리
            dq, dp = d_now % ((N - 1) * 2), d_now % ((M - 1) * 2)
            up = down = q
            up_d, down_d = 0, 1
            for _ in range(dq):
                if up == 1:
                    up_d = 1
                elif up == N:
                    up_d = 0
                if up_d == 0:
                    up -= 1
                else:
                    up += 1

                if down == 1:
                    down_d = 1
                elif down == N:
                    down_d = 0
                if down_d == 0:
                    down -= 1
                else:
                    down += 1

            left = right = p
            left_d, right_d = 0, 1
            for _ in range(dp):
                if left == 1:
                    left_d = 1
                elif left == N:
                    left_d = 0
                if left_d == 0:
                    left -= 1
                else:
                    left += 1

                if right == 1:
                    right_d = 1
                elif right == N:
                    right_d = 0
                if right_d == 0:
                    right -= 1
                else:
                    right += 1
            # 상, 하, 좌, 우
            move = [[up, p],
                    [down, p],
                    [q, left],
                    [q, right]]
            move.sort(key=lambda x: (-(x[0] + x[1]), -x[0], -x[1]))
            rabbits[0][1:4] = (move[0][0] + move[0][1]), move[0][0], move[0][1]
            rabbits[0][0] += 1

            for rabbit in rabbits[1:]:
                rabbit[6] += (move[0][0] + move[0][1])

        rabbits.sort(key=lambda x: (-x[1], -x[2], -x[3], -x[4]))
        for rabbit in rabbits:
            if rabbit[4] in picked:
                rabbit[6] += play[2]

    else:  # 이동거리 변경
        for rabbit in rabbits:
            if rabbit[4] == play[1]:
                rabbit[5] *= play[2]

last = input()
print(rabbits)