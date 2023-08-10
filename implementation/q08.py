"""
p.325 자물쇠와 열쇠
프로그래머스에 동일 문제 존재
"""

KEY = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]

LOCK = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]


# True


def solution(key, lock):
    def get_full_lock(lock_matrix):
        lock_matrix_size = len(lock_matrix)
        new_lock = [[0] * lock_matrix_size * 3 for _ in range(lock_matrix_size * 3)]
        for i in range(lock_matrix_size):
            for j in range(lock_matrix_size):
                new_lock[lock_matrix_size + i][lock_matrix_size + j] = lock[i][j]
        return new_lock

    def rotate_matrix_clockwise(key_matrix):
        key_matrix_size = len(key_matrix)
        new_matrix = [[0] * key_matrix_size for _ in range(key_matrix_size)]
        for i in range(key_matrix_size):
            for j in range(key_matrix_size):
                new_matrix[j][key_matrix_size - 1 - i] = key_matrix[i][j]
        return new_matrix

    def is_work(new_lock_matrix):
        lock_matrix_size = len(new_lock_matrix) // 3

        for i in range(lock_matrix_size, lock_matrix_size * 2):
            for j in range(lock_matrix_size, lock_matrix_size * 2):
                if new_lock_matrix[i][j] != 1:
                    return False
        return True

    key_size = len(key)
    lock_size = len(lock)
    rotated_key = key
    new_lock = get_full_lock(lock)

    for _ in range(4):
        rotated_key = rotate_matrix_clockwise(rotated_key)
        # 자물쇠가 조금이라도 겹치게 탐색 범위를 설정 (0부터 순회할 필요가 없음)
        for i in range(1, lock_size * 2):
            for j in range(1, lock_size * 2):
                # 자물쇠에 열쇠가 들어 맞는지 확인
                for row in range(key_size):
                    for column in range(key_size):
                        new_lock[i + row][j + column] += rotated_key[row][column]
                if is_work(new_lock):
                    return True
                for row in range(key_size):
                    for column in range(key_size):
                        new_lock[i + row][j + column] -= rotated_key[row][column]

    return False


print(solution(KEY, LOCK))
