"""
p.99 1이 될 때까지
"""

INPUT1 = "25 5"  # 2


def solution(input1):
    n, k = map(int, input1.split())
    start = n  # 25
    count = 0
    while True:
        # N을 K의 배수로 만들고, 그만큼 count에 더하기
        target = (start // k) * k
        count += (start - target)
        start = target
        # N이 K보다 작아지면 반복문 종료
        if start < k:
            break
        count += 1
        # 다음 나눗셈을 수행하기 위해 start를 k로 나눈 몫을 남김
        start //= k

    count += (start - 1)
    return count


print(solution(INPUT1))
