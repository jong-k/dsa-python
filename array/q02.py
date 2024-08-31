"""
프로그래머스
42889 실패율
"""

def solution(N, stages):
    fail_users = {}
    user_count = len(stages)

    for i in range(1, N + 1):
        fail_users[i] = 0

    for stage in stages:
        if stage <= N and stage in fail_users:
            fail_users[stage] += 1

    for i in range(1, N + 1):
        if fail_users[i] > 0:
            users = fail_users[i]
            fail_users[i] = fail_users[i] / user_count
            user_count -= users
        else:
            fail_users[i] = 0

    return [key for key, _ in sorted(fail_users.items(), key=lambda x: x[1], reverse=True)]
