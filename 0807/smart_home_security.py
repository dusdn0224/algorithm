T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    # sample에서 탐색을 시작할 위치
    s = 0
    # passcode의 길이와 같은지 확인할 카운트
    cnt = 0

    for i in range(K):
        for j in range(s, N):
            # passcode의 숫자 발견 시
            if sample[j] == passcode[i]:
                # 시작 위치를 그 다음으로 변경
                s = j + 1
                cnt += 1
                break

    # 출력할 값
    ans = 0
    # 카운트가 passcode의 길이와 같다면 생성 가능
    if cnt == K:
        ans = 1

    print(f'#{tc}', ans)

    # cnt = 0
    # result = 0
    # for i in range(N):
    #     if passcode[cnt] == sample[i]:
    #         cnt += 1
    #     if cnt == K:
    #         result = 1
    #         break
'''
2
10 4
1 1 2 2 3 3 4 4 5 5
1 2 3 4
7 4
1 2 2 4 3 3 4
4 3 2 1
'''