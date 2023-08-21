"""
파이써닉 퀵 정렬
"""
array1 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    # pivot 보다 무조건 작은 좌측 리스트
    left_side = [x for x in tail if x <= pivot]
    # pivot 보다 무조건 큰 우측 리스트
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
