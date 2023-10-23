"""
p.323 문자열 압축
"""


def solution(s):
    min_len = len(s)
    # 최대 절반으로 문자열을 정할 수 있음, 짝수로만 순회
    for i in range(1, len(s) // 2 + 1):
        zipped_str = ""  # 압축된 문자열
        acc_count = 1  # 누적 카운트
        cur_str = s[:i]  # 비교 단위 문자열
        # 비교 단위별 순회
        for j in range(i, len(s), i):
            # 현재 문자와 다음 문자가 같으면 누적 +1
            if cur_str == s[j:j + i]:
                acc_count += 1
            else:
                if acc_count > 1:
                    zipped_str += str(acc_count)
                    acc_count = 1
                    cur_str = s[j:j + i]
                # 문자를 압축된 문자열에 더해줌
                zipped_str += cur_str
        # 루프가 끝나고 맨 마지막 경우를 처리해줌
        if acc_count > 1:
            zipped_str += str(acc_count)
        # 문자를 압축된 문자열에 더해줌
        zipped_str += cur_str
        min_len = min(min_len, len(zipped_str))
    return min_len


print(solution("aabbaccc"))  # 7
