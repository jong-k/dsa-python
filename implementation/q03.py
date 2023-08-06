"""
p.115 왕실의 나이트
"""


def solution(pos):  # a1 = xy
    x, y = ord(pos[0]) - 96, int(pos[1])
    count = 0
    # 상하좌우
    dxdy = [(1, -2), (-1, -2), (-1, 2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if nx < 1 or nx > 8 or ny < 1 or ny > 8:
            continue
        count += 1
    return count


print(solution("a1"))  # 2
