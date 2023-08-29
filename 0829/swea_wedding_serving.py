from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, R = map(int, input().split())
    food = deque(map(int, input().split()))
    for _ in range(N):
        if list(food)[:(R * 2) + 1].count(food[0]) > 2:
            print(f'#{tc} NO')
            break
        food.append(food.popleft())
    else:
        print(f'#{tc} YES')
