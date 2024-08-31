"""
프로그래머스
12949 행렬의 곱셈
"""

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            res = 0
            for k in range(len(arr1[0])):
                res += arr1[i][k] * arr2[k][j]
            answer[i].append(res)

    return answer