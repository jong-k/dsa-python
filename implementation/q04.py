"""
p.118 게임 개발
"""

INPUT1 = ("4 4\n"
          "1 1 0\n"
          "1 1 1 1\n"
          "1 0 0 1\n"
          "1 1 0 1\n"
          "1 1 1 1\n")


def solution(input1):
    """
    y: 현재 y좌표\n
    x: 현재 x좌표\n
    direction: 북동남서에 따라 0123 순으로 값을 가짐\n
    board: 2차원 리스트\n
    dy: 북동남서 이동 y값\n
    dx: 북동남서 이동 x값\n
    move_count: 방문한 면적 수\n
    rest_count: 회전 가능한 횟수 (기본값 4)
    """
    data_list = input1.strip().split("\n")
    # 북동남서 = 0123
    y, x, direction = map(int, data_list[1].split())
    board = list(map(lambda k: list(map(int, k.split())), data_list[2:]))
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    move_count = 1
    rest_count = 4

    def rotate_left():
        """
        :return: 왼쪽으로 회전된 direction
        """
        nonlocal direction
        direction -= 1
        if direction == -1:
            direction = 3
        return direction

    while True:
        board[y][x] = 2  # 방문한 좌표를 2로 바꿈
        while rest_count > 0:
            direction = rotate_left()
            rest_count -= 1
            y += dy[direction]  # 바라보는 방향으로 이동
            x += dx[direction]  # 바라보는 방향으로 이동
            if board[y][x] == 0:
                rest_count = 4
                move_count += 1
                break
            y -= dy[direction]  # 갈 수 없으면 다시 후진
            x -= dx[direction]  # 갈 수 없으면 다시 후진
        if rest_count == 0:
            rest_count = 4
            # 모든 회전후 다시 원래 방향이 되면 후진
            # 후진하려는데 뒤가 바다이면 멈추고 종료
            y -= dy[direction]
            x -= dx[direction]
            if board[y][x] == 1:
                # print(board) # board 확인용
                return move_count


print(solution(INPUT1))  # 3
