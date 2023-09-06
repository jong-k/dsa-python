"""
p.376 정수 삼각형
백준 1932
"""
import sys

triangle_size = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(triangle_size)]


def solution(data):
    if len(data) == 1:
        return data[0][0]

    for i in range(1, len(data)):
        for j in range(len(data[i])):
            if j == 0:
                data[i][j] += data[i - 1][j]
            elif j == len(data[i]) - 1:
                data[i][j] += data[i - 1][j - 1]
            else:
                data[i][j] += max(data[i - 1][j - 1], data[i - 1][j])
    return max(data[-1])


print(solution(triangle))
