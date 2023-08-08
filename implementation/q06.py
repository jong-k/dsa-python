"""
p.322 문자열 재정렬
"""


def solution(s):
    char_list = []
    total = 0
    for char in s:
        if char.isnumeric():
            total += int(char)
        else:
            char_list.append(char)

    return "".join(sorted(char_list)) + str(total) if total > 0 else "".join(sorted(char_list))


print(solution("K1KA5CB7"))  # ABCKK13
print(solution("AJKDLSI412K4JSJ9D"))  # ADDIJJJKKLSS20
