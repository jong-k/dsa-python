"""
p.370 가사 검색
프로그래머스 lv.4
"""
from bisect import bisect_left, bisect_right

WORDS = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
QUERIES = ["fro??", "????o", "fr???", "fro???", "pro?"]


# 이진 탐색 버전
# 이진 탐색을 수행할 배열은 정렬되어 있어야 한다 -> 쿼리에 앞에서부터 매칭되는 단어들이 모두 연속되어 있음!
# 와일드카드가 앞에서 등장하는 쿼리들은? 단어들과 쿼리를 뒤집어서 실행하면 됨 -> 이러면 단어들을 연속되게 만들 수 있음!
def count_by_range(arr, left_val, right_val):
    """
    배열에서 연속된 원소의 갯수를 반환 
    :param arr: 배열
    :param left_val: 연속된 구간의 시작 인덱스를 찾을 값
    :param right_val: 연속된 구간의 마지막 인덱스 + 1 을 찾을 값
    :return: 연속된 원소의 갯수
    """
    # right_val을 배열에 삽입할 수 있는 인덱스 (즉, 연속된 구간의 다음 인덱스)
    right_idx = bisect_right(arr, right_val)
    # left_val을 배열에 삽입할 수 있는 인덱스 (즉, 연속된 구간의 시작 인덱스)
    left_idx = bisect_left(arr, left_val)
    return right_idx - left_idx


# 각 가사 단어의 길이는 1 이상 1만 이하
array_by_length = [[] for _ in range(10001)]
# 접두사 와일드카드를 위해 뒤집는 형태로 저장
reversed_array_by_length = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array_by_length[len(word)].append(word)
        reversed_array_by_length[len(word)].append(word[::-1])  # 단어를 뒤집어서 삽입

    for i in range(10001):
        array_by_length[i].sort()
        reversed_array_by_length[i].sort()

    for query in queries:
        # 와일드카드가 앞에 오면 뒤집어서 탐색
        # 쿼리 "o??" 는 "oaa" ~ "ozz" 까지 가능
        if query[0] == "?":
            match_cnt = count_by_range(reversed_array_by_length[len(query)], query[::-1].replace("?", "a"),
                                       query[::-1].replace("?", "z"))
        else:
            match_cnt = count_by_range(array_by_length[len(query)], query.replace("?", "a"),
                                       query.replace("?", "z"))
        answer.append(match_cnt)
    return answer


print(solution(WORDS, QUERIES))  # [3, 2, 4, 1, 0]
