"""
p.178 위에서 아래로
"""

input1 = ("3\n"
          "15\n"
          "27\n"
          "12")


def solution(data):
    data = list(map(int, data.split("\n")))
    # popleft
    data.pop(0)
    return " ".join(map(str, sorted(data, reverse=True)))


print(solution(input1))  # 27 15 12
