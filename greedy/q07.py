"""
p. 문자열 뒤집기
"""

S = "0001100"  # 1
# S = "01010101" # 4
"""풀이
0으로 통일하는 경우의 수와 1로 통일하는 경우의 수를 비교하면 된다
첫 문자열을 확인하여 0, 1 카운트를 1 증가시킨다
이후 문자열이 달라지면, 달라진 문자열의 카운트를 1 증가시킨다
마지막에 작은 횟수를 답으로 출력한다 
"""

"""그리디 알고리즘인 이유
비교할 대상이 2가지 밖에 없어서 (0, 1)
0, 1 중에 횟수가 작은 것이 답이라서?
"""


def solution(s):
    count_dict = {"0": 0, "1": 0}
    current_char = s[0]
    count_dict[current_char] += 1
    for char in s:
        if char != current_char:
            count_dict[char] += 1
            current_char = char
    return min(count_dict["0"], count_dict["1"])


print(solution(S))
