"""
p.149 음료수 얼려 먹기
프로그래머스 네트워크
"""
from collections import deque

Height = 4
Width = 5
# 0: 구멍이 뚫린 부분 -> 얼음 생성 가능
# 1: 막힌 부분
INPUT1 = ("00110\n"
          "00011\n"
          "11111\n"
          "00000")
# 3
INPUT2 = ("10101\n"
          "01010\n"
          "10101\n"
          "01010")


# 10


def solution(height, width, input1):
    queue = deque()
    board = list(map(lambda x: list(x), input1.split("\n")))
    # 동서남북
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    answer = 0

    def bfs(y, x):
        nonlocal answer
        queue.append((y, x))
        board[y][x] = "1"  # 방문 처리를 0 -> 1로 대체
        while queue:
            node = queue.popleft()  # (y, x)
            for i in range(4):
                ny = node[0] + dy[i]
                nx = node[1] + dx[i]
                if 0 <= ny < height and 0 <= nx < width:
                    if board[ny][nx] == "0":
                        queue.append((ny, nx))
                        board[ny][nx] = "1"
        answer += 1

    for row in range(height):
        for column in range(width):
            if board[row][column] == "0":
                bfs(row, column)
    return answer


print(solution(Height, Width, INPUT2))
