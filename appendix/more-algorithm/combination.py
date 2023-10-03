from itertools import combinations

# [1, 2, 3, 4] 에서 2개를 뽑는 경우의 수
for x in combinations([1, 2, 3, 4], 2):
    print(x)

"""
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
"""
