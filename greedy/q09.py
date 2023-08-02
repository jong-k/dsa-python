"""
p.315 볼링공 고르기
"""
# INPUT1 = "5 3"
# INPUT2 = "1 3 2 3 2"  # sort -> 1 2 2 3 3


# 8

"""풀이
오름차순으로 수열을 정렬하고
중첩 반복문을 만들어 앞, 뒤 숫자를 비교하여 뒤의 숫자가 앞의 숫자보다 더 크면 +1 시킨다
"""

"""그리디 알고리즘인 이유
오름차순 정렬한 후 앞에서부터 비교해나가기 때문에
정답일 가능성이 크다?
"""

INPUT1 = "8 5"
INPUT2 = "1 5 4 3 2 4 5 2"


# 25

def solution(input1, input2):
    balls_total, max_weight = map(int, input1.split(" "))
    balls_list = sorted(list(map(int, input2.split(" "))))
    pairs = 0
    for i in range(balls_total):
        for j in range(i + 1, balls_total):
            if balls_list[j] > balls_list[i]:
                pairs += 1
    return pairs


print(solution(INPUT1, INPUT2))
