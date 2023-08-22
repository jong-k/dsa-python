"""
계수 정렬
"""
# 데이터가 양의 정수라고 가정
arr1 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]


def count_sort(arr):
    # (편의상) 0부터 데이터 최댓값 까지의 빈도 수를 기록할 리스트 선언
    count_list = [0] * (max(arr) + 1)
    answer = []
    for i in arr:
        count_list[i] += 1
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            answer.append(i)
    return answer


print(count_sort(arr1))  # [0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
