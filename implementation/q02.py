"""
p.113 시각
"""


def solution(n):
    count = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if "3" in str(h) + str(m) + str(s):
                    count += 1
    return count


print(solution(5))  # 11475
