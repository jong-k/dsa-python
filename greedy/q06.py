"""
p.312 곱하기 혹은 더하기
"""

# S = "02984" # 576
S = "567"  # 210
"""풀이
0, 1 일 때는 무조건 더해야 하고 나머지 숫자는 곱하면 됨
"""

"""그리디 알고리즘인 이유
일반적으로 0이나 1은 곱셈보다 덧셈이 유리하고,
나머지 숫자는 곱하면 커지기 때문에 지금 상황에서 일단 좋아보이는 그리디 알고리즘과 일치
"""


def solution(s):
    answer = 0
    for x in s:
        num = int(x)
        if num <= 1 or answer <= 1:
            answer += num
        else:
            answer *= num
    return answer


print(solution(S))
