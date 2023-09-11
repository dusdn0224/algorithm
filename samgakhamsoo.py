import math

start = (1, 1)
end = (3, 3)
goal = (5, 7)

y = abs(goal[0] - start[0])
x = abs(goal[1] - start[1])

a = math.sqrt(y ** 2 + x ** 2)

ga = math.atan(15 / 5)

print(a, math.degrees(ga))
