"""
삽입 정렬
"""

arr1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def insertion_sort(arr):
    # 삽입할 원소 인덱스
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            # 삽입할 원소가 기존 원소보다 적으면 앞으로 1칸 이동
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:  # 자기보다 작은 원소를 만나면 순회 종료
                break
    return arr


print(insertion_sort(arr1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
