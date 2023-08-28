"""
p.201 떡볶이 떡 만들기
"""

input1 = ("4 6\n"
          "19 15 10 17")


def calc_length(array, height):
    """
    :param array: 떡 길이 리스트
    :param height: 절단기 높이
    :return: 잘린 떡들의 길이 총합
    """
    result = 0
    for len_num in array:
        result += len_num - height if height < len_num else 0
    return result


def binary_search(array, target, start, end):
    """
    :param array: 떡 길이 리스트
    :param target: 손님이 요청한 떡 길이
    :param start: 0에서 시작
    :param end: 떡 길이 리스트에서 최댓값에서 시작
    :return: 이진 탐색 결과 반환
    """
    mid = 0

    while start <= end:
        mid = (start + end) // 2

        if calc_length(array, mid) == target:
            return mid
        elif calc_length(array, mid) > target:
            start = mid + 1
        else:
            end = mid - 1
    return mid  # 높이의 최댓값 출력


def solution(data):
    data = data.split("\n")
    data_size, target_num = map(int, data[0].split())
    data_list = list(map(int, data[1].split()))
    max_num = max(data_list)

    return binary_search(data_list, target_num, 0, max_num)


print(solution(input1))  # 15
