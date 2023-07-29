N = 5
VALUES = "2 3 1 2 2"
# VALUES = 3 4 이면 0 출력

"""
VALUES를 오름차순으로 정렬한다
맨 뒤의 가장 큰 숫자를 pop 한다
popped - 1 만큼 VALUES에서 pop 반복 (이 때 VALUES에 남은 원소가 없으면 반복을 종료하고 결과를 반환)
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
