import math
import time

start = time.time()  # 시작 시간 측정


def fib(num):
    """
    피보나치 수열의 n항을 구하는 함수
    :param num: n
    :return: n항의 값
    """
    if num == 1 or num == 2:
        return 1
    return fib(num - 1) + fib(num - 2)


print(fib(40))  # 102334155
end = time.time()  # 종료 시간 측정
print(f"{end - start:.5f} sec")  # 11.61979 sec
