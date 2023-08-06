"""
p.110 상하좌우
"""
import time

start = time.time()

INPUT1 = 5
INPUT2 = "R R R U D D"


def solution(n, directions):
    direction_list = directions.split()
    current_pos = [1, 1]
    for direction in direction_list:
        if direction == "U":
            if current_pos[0] > 1:
                current_pos[0] -= 1
        elif direction == "D":
            if current_pos[0] < n:
                current_pos[0] += 1
        elif direction == "L":
            if current_pos[1] > 1:
                current_pos[1] -= 1
        elif direction == "R":
            if current_pos[1] < n:
                current_pos[1] += 1
    return current_pos


print(*solution(INPUT1, INPUT2))
end = time.time()
print(f"time: {end - start:.5f}s")  # 수행시간 측정 불가 0.0000s
