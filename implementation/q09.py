"""
p.327 뱀
백준 3190 뱀
"""

board_size = int(input())
apple_num = int(input())
apple_list = [list(map(int, input().split())) for _ in range(apple_num)]
move_num = int(input())
move_list = [input().split() for _ in range(move_num)]
for i in range(move_num):
    move_list[i][0] = int(move_list[i][0])

# 뱀의 몸통을 좌표로 갖는 배열
snake_body = [
    [1, 1]
]
# 시계방향으로 상우하좌 -> turn을 편하게 하기 위해
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# 처음엔 우로 이동
current_direction = 1
second = 0


def turn(turn_type):
    """
    L or D 를 입력받아 current_direction을 변경
    :param turn_type: L or D
    """
    global current_direction
    if turn_type == "L":
        current_direction -= 1
        if current_direction == -1:
            current_direction = 3
    else:
        current_direction += 1
        if current_direction == 4:
            current_direction = 0


while True:
    second += 1
    # 새로운 머리 좌표
    new_y = snake_body[0][0] + dy[current_direction]
    new_x = snake_body[0][1] + dx[current_direction]
    # 벽에 충돌하면 종료
    if new_y <= 0 or new_y > board_size or new_x <= 0 or new_x > board_size:
        break
    # 자기 몸에 충돌하면 종료
    if [new_y, new_x] in snake_body:
        break
    # 사과를 만나면 크기 증가
    if [new_y, new_x] in apple_list:
        apple_list.remove([new_y, new_x])
    else:
        # 사과가 아니면 꼬리 하나 자름
        snake_body.pop()

    # 방향 업데이트
    for i in range(move_num):
        if second == move_list[i][0]:
            turn(move_list[i][1])
            break

    # 새 머리를 맨 앞에 추가
    snake_body.insert(0, [new_y, new_x])

print(second)
