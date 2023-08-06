"""
p.99 1이 될 때까지
"""

INPUT = "25 5"  # 2


def solution(input1):
    n, k = map(int, input1.split())
    start = n
    count = 0
    while start != 1:
        if start % k == 0:
            start = int(start / k)
        else:
            start -= 1
        count += 1
    return count


print(solution(INPUT))
