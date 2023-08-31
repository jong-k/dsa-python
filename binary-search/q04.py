"""
고정점 찾기
"""

input1 = [-15, -6, 1, 3, 7]
input2 = [1, 3, 5, 7, 9]
input3 = [2, 4, 6, 8, 10]


def binary_search(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        # 원소가 인덱스보다 크면 다음 범위 확인 불필요
        elif arr[mid] > mid:
            end = mid - 1
        # 원소가 인덱스보다 작으면 이전 범위 확인 불필요
        else:
            start = mid + 1
    # 고정점이 없으면 -1 반환
    return -1


print(binary_search(input1))  # 3
print(binary_search(input2))  # -1
print(binary_search(input3))  # -1
