"""
p. 367 정렬된 배열에서 특정 수의 갯수 구하기
"""
from bisect import bisect_left, bisect_right

input1 = ("7 2\n"
          "1 1 2 2 2 2 3")

input2 = ("7 4\n"
          "1 1 2 2 2 2 3")


def solution(data):
    data = data.split("\n")
    array_size, target = map(int, data[0].split())
    array = sorted(list(map(int, data[1].split())))
    left_idx = bisect_left(array, target)
    right_idx = bisect_right(array, target)
    if right_idx - left_idx == 0:
        print(-1)
    else:
        print(right_idx - left_idx)


solution(input1)  # 4
solution(input2)  # -1
