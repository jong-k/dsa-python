"""
프로그래머스
42840 모의고사
"""


def solution(answers):
    scores = [0, 0, 0]

    def get_score_a(idx):
        return (idx % 5) + 1

    def get_score_b(idx):
        if idx % 2 == 0:
            return 2
        elif idx % 8 == 1:
            return 1
        elif idx % 8 == 3:
            return 3
        elif idx % 8 == 5:
            return 4
        elif idx % 8 == 7:
            return 5

    def get_score_c(idx):
        if idx % 10 in (0, 1):
            return 3
        elif idx % 10 in (2, 3):
            return 1
        elif idx % 10 in (4, 5):
            return 2
        elif idx % 10 in (6, 7):
            return 4
        else:
            return 5

    for index, value in enumerate(answers):
        if value == get_score_a(index):
            scores[0] += 1
        if value == get_score_b(index):
            scores[1] += 1
        if value == get_score_c(index):
            scores[2] += 1

    max_score = max(scores)
    return sorted([i + 1 for i, v in enumerate(scores) if v == max_score])
