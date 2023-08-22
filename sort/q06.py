"""
p.361 실패율
프로그래머스
"""
n = 5
Stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):
    ratio_list = []

    for i in range(1, N + 1):
        no_clears = stages.count(i)
        reaches = len([x for x in stages if x >= i])
        if reaches != 0:
            ratio_list.append((i, no_clears / reaches))
        else:
            ratio_list.append((i, 0))

    ratio_list.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in ratio_list]


print(solution(n, Stages))
