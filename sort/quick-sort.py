"""
퀵 정렬
"""
array1 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    # 배열의 길이가 1이면 종료
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # left는 왼쪽에서 오른쪽으로 pivot보다 큰 값을 찾음 (end +1 까지 가능)
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # right는 오른쪽에서 왼쪽으로 pivot보다 작은 값을 찾음 (pivot 까지 가능)
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 엇갈렸으면 피벗보다 작은 원소(right)를 피벗과 스왑
        if right < left:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 아니면 작은 원소와 큰 원소를 스왑 (left <= right 이면 while loop 한 번 더 탐)
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


quick_sort(array1, 0, len(array1) - 1)
print(array1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
