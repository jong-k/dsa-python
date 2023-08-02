"""
p. 87 거스름돈
"""

N = 1260  # 6


def solution(n):
    count = 0
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += n // coin
        n %= coin
    return count


print(solution(N))
