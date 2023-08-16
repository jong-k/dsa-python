"""
p.152 미로 탈출
"""
from collections import deque

Height = 5
Width = 6
# 0: 막힌 부분
# 1: 갈 수 있는 부분
INPUT1 = ("101010\n"
          "111111\n"
          "000001\n"
          "111111\n"
          "111111")


def solution(height, width, input1):
    queue = deque([(0, 0)])
    board = list(map(lambda x: list(x), input1.split("\n")))
    # 시작점 (0, 0) 에서부터의 거리를 기록할 2차원 리스트
    count_board = [[0] * width for _ in range(height)]
    count_board[0][0] = 1
    # 동서남북
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    def bfs():
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < height and 0 <= nx < width and board[ny][nx] == "1" and count_board[ny][nx] == 0:
                    queue.append((ny, nx))
                    count_board[ny][nx] = count_board[y][x] + 1
        return count_board[height - 1][width - 1]

    return bfs()


print(solution(Height, Width, INPUT1))
