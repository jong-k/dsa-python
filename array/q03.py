"""
프로그래머스
방문 길이 49994
"""

def solution(dirs):
    set1 = set()
    start = [5, 5]

    for direction in dirs:
        to = [start[0], start[1]]

        if direction == "U":
            to[0] += 1
        if direction == "D":
            to[0] -= 1
        if direction == "L":
            to[1] -= 1
        if direction == "R":
            to[1] += 1

        if to[0] < 0 or to[0] > 10 or to[1] < 0 or to[1] > 10:
            continue

        set1.add(tuple(start + to))
        set1.add(tuple(to + start))
        start = to

    return len(set1) / 2
