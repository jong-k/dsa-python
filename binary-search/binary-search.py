"""
이진 탐색 (반복문)
"""
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if (array[mid] == target):
            return mid
        elif (array[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    print("원소가 존재하지 않습니다")
    return None


print(binary_search(data, 15))  # 7
