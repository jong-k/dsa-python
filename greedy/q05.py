"""
p.311 모험가 길드
"""

N = 5
VALUES = "2 3 1 2 2"
# VALUES = 3 4 이면 0 출력

"""풀이과정
VALUES를 오름차순으로 정렬한다
맨 뒤의 가장 큰 숫자를 pop 한다
popped - 1 만큼 VALUES에서 pop 반복 (이 때 VALUES에 남은 원소가 없으면 반복을 종료하고 결과를 반환)
"""

"""이문제가 그리디인 이유
가장 큰 수들을 먼저 처리하기 때문에 (가장 작은 1의 경우 1 하나로도 그룹 하나 생성 가능)
지금 상황에서 가장 좋아 보이는 것을 처리하는 그리디와 일맥상통
"""


def solution(values):
    sorted_values = sorted(map(int, values.split(" ")))
    print(sorted_values)
    result = 0

    while len(sorted_values) > 0:
        popped = sorted_values.pop()
        for x in range(popped - 1):
            if len(sorted_values) == 0:
                return result
            sorted_values.pop()
        result += 1

    return result


print(solution(VALUES))
