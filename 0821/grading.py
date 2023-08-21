T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_grade = 0
    min_grade = M * M
    for student in arr:
        grade = 0
        point = 0
        for i in range(M):
            if student[i] == answer[i]:
                point += 1
                grade += point
            else:
                point = 0
        if max_grade < grade:
            max_grade = grade
        if min_grade > grade:
            min_grade = grade
    print(f'#{tc}', max_grade - min_grade)
