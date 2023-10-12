n = int(input())
# U: 위 D: 아래 F: 앞 B: 뒤 L: 왼 R: 오
def rotate(face, direction):
    if face == 'U':
        if direction == '+':
            lst = [[og[0][2][0], og[0][1][0], og[0][0][0]],
                   [og[0][2][1], og[0][1][1], og[0][0][1]],
                   [og[0][2][2], og[0][1][2], og[0][0][2]]]
            og[0] = lst
            save = og[2][0]
            og[2][0] = og[5][0]
            og[5][0] = og[3][0]
            og[3][0] = og[4][0]
            og[4][0] = save
        else:
            lst = [[og[0][0][2], og[0][1][2], og[0][2][2]],
                   [og[0][0][1], og[0][1][1], og[0][2][1]],
                   [og[0][0][0], og[0][1][0], og[0][2][0]]]
            og[0] = lst
            save = og[2][0]
            og[2][0] = og[4][0]
            og[4][0] = og[3][0]
            og[3][0] = og[5][0]
            og[5][0] = save
    elif face == 'D':
        if direction == '+':
            lst = [[og[1][2][0], og[1][1][0], og[1][0][0]],
                   [og[1][2][1], og[1][1][1], og[1][0][1]],
                   [og[1][2][2], og[1][1][2], og[1][0][2]]]
            og[1] = lst
            save = og[2][2]
            og[2][2] = og[4][2]
            og[4][2] = og[3][2]
            og[3][2] = og[5][2]
            og[5][2] = save
        else:
            lst = [[og[1][0][2], og[1][1][2], og[1][2][2]],
                   [og[1][0][1], og[1][1][1], og[1][2][1]],
                   [og[1][0][0], og[1][1][0], og[1][2][0]]]
            og[1] = lst
            save = og[2][2]
            og[2][2] = og[5][2]
            og[5][2] = og[3][2]
            og[3][2] = og[4][2]
            og[4][2] = save
    elif face == 'F':
        if direction == '+':
            lst = [[og[2][2][0], og[2][1][0], og[2][0][0]],
                   [og[2][2][1], og[2][1][1], og[2][0][1]],
                   [og[2][2][2], og[2][1][2], og[2][0][2]]]
            og[2] = lst
            save = og[0][2]
            og[0][2] = [og[4][2][2], og[4][1][2], og[4][0][2]]
            for i in range(3):
                og[4][i][2] = og[1][2][i]
            og[1][2] = [og[5][2][0], og[5][1][0], og[5][0][0]]
            for i in range(3):
                og[5][i][0] = save[i]
        else:
            lst = [[og[2][0][2], og[2][1][2], og[2][2][2]],
                   [og[2][0][1], og[2][1][1], og[2][2][1]],
                   [og[2][0][0], og[2][1][0], og[2][2][0]]]
            og[2] = lst
            save = og[0][2]
            og[0][2] = [og[5][0][0], og[5][1][0], og[5][2][0]]
            for i in range(3):
                og[5][i][0] = og[1][2][2 - i]
            og[1][2] = [og[4][0][2], og[4][1][2], og[4][2][2]]
            for i in range(3):
                og[4][2 - i][2] = save[i]
    elif face == 'B':
        if direction == '+':
            lst = [[og[3][2][0], og[3][1][0], og[3][0][0]],
                   [og[3][2][1], og[3][1][1], og[3][0][1]],
                   [og[3][2][2], og[3][1][2], og[3][0][2]]]
            og[3] = lst
            save = og[0][0]
            og[0][0] = [og[5][0][2], og[5][1][2], og[5][2][2]]
            for i in range(3):
                og[5][i][2] = og[1][0][2 - i]
            og[1][0] = [og[4][0][0], og[4][1][0], og[4][2][0]]
            for i in range(3):
                og[4][2 - i][0] = save[i]
        else:
            lst = [[og[3][0][2], og[3][1][2], og[3][2][2]],
                   [og[3][0][1], og[3][1][1], og[3][2][1]],
                   [og[3][0][0], og[3][1][0], og[3][2][0]]]
            og[3] = lst
            save = og[0][0]
            og[0][0] = [og[4][2][0], og[4][1][0], og[4][0][0]]
            for i in range(3):
                og[4][i][0] = og[1][0][i]
            og[1][0] = [og[5][2][2], og[5][1][2], og[5][0][2]]
            for i in range(3):
                og[5][i][2] = save[i]
    elif face == 'L':
        if direction == '+':
            lst = [[og[4][2][0], og[4][1][0], og[4][0][0]],
                   [og[4][2][1], og[4][1][1], og[4][0][1]],
                   [og[4][2][2], og[4][1][2], og[4][0][2]]]
            og[4] = lst
            save = [og[0][0][0], og[0][1][0], og[0][2][0]]
            for i in range(3):
                og[0][i][0] = og[3][2 - i][2]
            for i in range(3):
                og[3][i][2] = og[1][i][0]
            for i in range(3):
                og[1][i][0] = og[2][2 - i][0]
            for i in range(3):
                og[2][i][0] = save[i]
        else:
            lst = [[og[4][0][2], og[4][1][2], og[4][2][2]],
                   [og[4][0][1], og[4][1][1], og[4][2][1]],
                   [og[4][0][0], og[4][1][0], og[4][2][0]]]
            og[4] = lst
            save = [og[0][0][0], og[0][1][0], og[0][2][0]]
            for i in range(3):
                og[0][i][0] = og[2][i][0]
            for i in range(3):
                og[2][i][0] = og[1][2 - i][0]
            for i in range(3):
                og[1][i][0] = og[3][i][2]
            for i in range(3):
                og[3][i][2] = save[2 - i]
    elif face == 'R':
        if direction == '+':
            lst = [[og[5][2][0], og[5][1][0], og[5][0][0]],
                   [og[5][2][1], og[5][1][1], og[5][0][1]],
                   [og[5][2][2], og[5][1][2], og[5][0][2]]]
            og[5] = lst
            save = [og[0][0][2], og[0][1][2], og[0][2][2]]
            for i in range(3):
                og[0][i][2] = og[2][i][2]
            for i in range(3):
                og[2][i][2] = og[1][2 - i][2]
            for i in range(3):
                og[1][i][2] = og[3][i][0]
            for i in range(3):
                og[3][i][0] = save[2 - i]
        else:
            lst = [[og[5][0][2], og[5][1][2], og[5][2][2]],
                   [og[5][0][1], og[5][1][1], og[5][2][1]],
                   [og[5][0][0], og[5][1][0], og[5][2][0]]]
            og[5] = lst
            save = [og[0][0][2], og[0][1][2], og[0][2][2]]
            for i in range(3):
                og[0][i][2] = og[3][2 - i][0]
            for i in range(3):
                og[3][i][0] = og[1][i][2]
            for i in range(3):
                og[1][i][2] = og[2][2 - i][2]
            for i in range(3):
                og[2][i][2] = save[i]


for _ in range(n):
    og = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
          [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
          [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
          [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
          [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
          [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]]
    k = int(input())
    hows = list(input().split())
    for how in hows:
        rotate(how[0], how[1])
    for p in range(3):
        for q in range(3):
            print(og[0][p][q], end='')
        print()