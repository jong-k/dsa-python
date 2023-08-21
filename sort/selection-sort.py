"""
선택 정렬
"""

arr1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def selection_sort(arr):
    for i in range(len(arr)):
        # 가장 작은 원소 인덱스
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # 맨 앞의 정렬되지 않은 원소와 바꾸기
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


print(selection_sort(arr1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
