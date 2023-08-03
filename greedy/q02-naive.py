"""
p.92 큰 수의 법칙
"""
# INPUT1 = "5 8 3"
# INPUT2 = "2 4 5 4 6"


# 46

INPUT1 = "5 7 2"
INPUT2 = "3 4 3 4 3"


# 28


def solution(input1, input2):
    n, m, k = map(int, input1.split())
    data = sorted(list(map(int, input2.split())), reverse=True)
    total = 0
    count = k

    for i in range(m):
        if count > 0:
            count -= 1
            total += data[0]
        else:
            count = k
            total += data[1]
    return total


print(solution(INPUT1, INPUT2))
