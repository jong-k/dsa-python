import math
import time

start = time.time()  # 시작 시간 측정

memo = [0] * 101


def fib(num):
    memo[1] = 1
    memo[2] = 1

    for i in range(3, num + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[num]


print(fib(40))  # 102334155
end = time.time()  # 종료 시간 측정
print(f"{end - start:.5f} sec")  # 0.00000 sec
