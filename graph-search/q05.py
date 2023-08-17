"""
p.344 경쟁적 전염
백준 18405 골5
"""
import sys
from collections import deque


def solution():
    board_size, virus_num = map(int, sys.stdin.readline().rstrip().split())
    board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(board_size)]
    target_time, target_row, target_col = map(int, sys.stdin.readline().rstrip().split())
    queue = deque()
    visited = [[False] * board_size for _ in range(board_size)]
    # 동서남북
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    # 큐에 초기값 삽입
    for i in range(board_size):
        for j in range(board_size):
            # 바이러스가 존재하는 좌표
            if board[i][j] != 0 and not visited[i][j]:
                # 큐에 (현재 바이러스 번호, row, col) 튜플 삽입
                queue.append((board[i][j], i, j))
                visited[i][j] = True

    while target_time:
        target_time -= 1

        # 큐에 바이러스 좌표들 있는 상태에서 오름차순 정렬
        queue = deque(sorted(queue, key=lambda x: x[0]))
        for _ in range(len(queue)):
            current_virus, y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < board_size and 0 <= nx < board_size:
                    if board[ny][nx] == 0 and not visited[ny][nx]:
                        # 바이러스 확산
                        board[ny][nx] = current_virus
                        visited[ny][nx] = True
                        queue.append((current_virus, ny, nx))

    return board[target_row - 1][target_col - 1]


print(solution())
