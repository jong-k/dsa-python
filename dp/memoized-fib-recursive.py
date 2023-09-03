import math
import time

start = time.time()  # 시작 시간 측정

memo = [0] * 100


def fib(num):
    """
    피보나치 수열의 n항을 구하는 함수
    :param num: n
    :return: n항의 값
    """
    if num == 1 or num == 2:
        return 1
    if memo[num]:
        return memo[num]
    memo[num] = fib(num - 1) + fib(num - 2)
    return memo[num]


print(fib(40))  # 102334155
end = time.time()  # 종료 시간 측정
print(f"{end - start:.5f} sec")  # 0.00000 sec
# 메모이제이션 도입 전에는 10초 넘게 걸렸지만 0초만에 실행 완료
