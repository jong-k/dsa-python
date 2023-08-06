"""
p.110 상하좌우
"""
import time

start = time.time()

INPUT1 = 5
INPUT2 = "R R R U D D"


def solution(n, directions):
    direction_list = directions.split()
    x, y = 1, 1

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    direction_types = ["U", "D", "L", "R"]

    for direction in direction_list:
        nx, ny = 0, 0
        for i in range(len(direction_types)):
            if direction == direction_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    return [x, y]


print(*solution(INPUT1, INPUT2))
end = time.time()
print(f"time: {end - start:.5f}s")  # 수행시간 측정 불가 0.0000s
