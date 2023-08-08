"""
p.321 럭키 스트레이트
"""


def solution(n):
    stringified_n = str(n)
    total_len = len(stringified_n)
    left_side = list(stringified_n[:total_len // 2])
    right_side = list(stringified_n[total_len // 2:])
    return "LUCKY" if sum(map(int, left_side)) == sum(map(int, right_side)) else "READY"


print(solution(123402))  # LUCKY
print(solution(7755))  # READY
