import math


def solution(n):
    """
    에라토스테네스의 체를 이용해 n 이하의 모든 소수 구하기
    :param n: 2이상의 자연수
    :return: 소수 배열
    """
    arr = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i]:
            for j in range(i * 2, n + 1, i):
                arr[j] = False
    return [i for i in range(2, n + 1) if arr[i]]


print(solution(100))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
