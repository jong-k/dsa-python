"""
못생긴 수
"""

"""풀이

"""


def solution(n):
    memo = [0] * (n + 1)
    memo[1] = 1
    # 저장된 못생긴 수에 x2, x3, x5 를 해 나가야 하므로,
    # 마지막으로 x2, x3, x5 한 인덱스를 기록
    i2 = i3 = i5 = 1
    # 못생긴 수에 x2, x3, x5 한 결과를 기록하는 변수
    next2, next3, next5 = 2, 3, 5

    for i in range(2, n + 1):
        # 오름차순으로 기록하기 위해 최솟값을 사용
        memo[i] = min(next2, next3, next5)

        if memo[i] == next2:
            i2 += 1
            next2 = memo[i2] * 2

        if memo[i] == next3:
            i3 += 1
            next3 = memo[i3] * 3

        if memo[i] == next5:
            i5 += 1
            next5 = memo[i5] * 5

    return memo[n]


print(solution(10))  # 12
print(solution(4))  # 4
