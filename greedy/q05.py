N = 5
VALUES = "2 3 1 2 2"


# VALUES = 3 4 이면 0 출력

def solution(values):
    """일단 정렬시키기"""
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
