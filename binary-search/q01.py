"""
p.197 부품 찾기
"""

input1 = ("5\n"
          "8 3 7 9 2\n"
          "3\n"
          "5 7 9")


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def solution(data):
    data = data.split("\n")
    parts = sorted(list(map(int, data[1].split())))
    required_parts = list(map(int, data[3].split()))

    for parts_id in required_parts:
        if binary_search(parts, parts_id) is None:
            print("no", end=" ")
        else:
            print("yes", end=" ")


solution(input1)  # no yes yes

"""시간 복잡도
N = 전체 데이터 갯수
M = 찾을 데이터 갯수
1. 전체 데이터 오름차순 정렬 : N * logN
2. 이진 탐색 M회 : M * logN
따라서 (N + M) * logN
"""
