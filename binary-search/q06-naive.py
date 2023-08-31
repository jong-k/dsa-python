"""
p.370 가사 검색
프로그래머스 lv.4
"""

WORDS = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
QUERIES = ["fro??", "????o", "fr???", "fro???", "pro?"]


# naive 풀이라서 효율성 테스트에서 막힘
def solution(words, queries):
    answer = []
    for query in queries:
        match_cnt = 0
        for word in words:
            if len(query) != len(word):
                continue
            is_match = True
            for i in range(len(query)):
                if query[i] == "?":
                    continue
                if query[i] != word[i]:
                    is_match = False
                    break
            if is_match:
                match_cnt += 1
        answer.append(match_cnt)
    return answer
