"""
p.92 큰 수의 법칙
"""
INPUT1 = "5 8 3"
INPUT2 = "2 4 5 4 6"


# 46

# INPUT1 = "5 7 2"
# INPUT2 = "3 4 3 4 3"
#
#
# # 28

def solution(input1, input2):
    n, m, k = map(int, input1.split())
    data = sorted(list(map(int, input2.split())), reverse=True)
    bundle = data[0] * k + data[1]  # 패턴
    bundle_num = m // (k + 1)  # 패턴이 몇 번 등장하는지
    rest = m % (k + 1)  # 나머지
    return bundle * bundle_num + rest * data[0]


print(solution(INPUT1, INPUT2))
