from itertools import permutations

# [1, 2, 3, 4] 에서 2개를 뽑아 나열하는 경우의 수
for x in permutations([1, 2, 3, 4], 2):
    print(x)

"""
(1, 2)
(1, 3)
(1, 4)
(2, 1)
(2, 3)
(2, 4)
(3, 1)
(3, 2)
(3, 4)
(4, 1)
(4, 2)
(4, 3)
"""
