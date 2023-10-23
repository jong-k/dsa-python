"""
p.314 만들 수 없는 금액
백준 2437 저울
"""

N = 5
COINS = "3 2 1 1 9"
# COINS = "1 2 5"

"""풀이
동전들을 작은 순으로 정렬하면 1 1 2 3 9
동전들 중에 1은 반드시 포함되어 있어야 한다.
따라서 앞, 뒤 순으로 동전이 있을 때, 뒤의 동전은 앞의 동전 +1 
"""


def solution(coins):
    sorted_coins = sorted(map(int, coins.split(" ")))
    possible_amount = 1
    for coin in sorted_coins:
        if coin > possible_amount:
            break
        else:
            possible_amount += coin
    return possible_amount


print(solution(COINS))
