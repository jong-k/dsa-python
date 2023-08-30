"""
p.369 공유기 설치
백준 2110
"""
import sys

house_num, target_num = map(int, sys.stdin.readline().split())
house_list = sorted(int(sys.stdin.readline()) for _ in range(house_num))


def calc_place_num(arr, distance):
    """
    이격 거리에 따른 최대 배치 가능 장소의 수를 계산
    :param arr: 좌표 리스트
    :param distance: 이격 거리
    :return: 최대 배치 가능 장소의 수
    """
    # 맨 앞에 우선 배치하고 시작
    current_place = arr[0]
    place_num = 1

    for i in range(len(arr)):
        # 이격거리를 만족하는 새 장소가 나타나면
        if arr[i] - current_place >= distance:
            # 배치 장소 +1
            place_num += 1
            current_place = arr[i]

    return place_num


def binary_search(arr, arr_size, target_place_num):
    """
    이진 탐색
    :param arr: 좌표 리스트
    :param arr_size: 좌표 리스트 크기
    :param target_place_num: 배치할 장소 갯수
    :return: 인접 거리의 최댓값
    """
    start = 0
    end = arr[arr_size - 1]
    max_neighbor_distance = 0
    while start <= end:
        mid = (start + end) // 2
        # 타겟 장소 갯수보다 여유가 있으면
        if calc_place_num(arr, mid) >= target_place_num:
            # 최댓값 갱신 후
            max_neighbor_distance = mid
            # 이격 거리 증가
            start = mid + 1
        else:
            end = mid - 1
    # 반복문이 끝나면 기록된 가장 최댓값 반환
    return max_neighbor_distance


print(binary_search(house_list, house_num, target_num))
