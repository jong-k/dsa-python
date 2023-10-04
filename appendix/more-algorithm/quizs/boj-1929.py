"""
p.485 소수 구하기
백준 1929
"""

"""풀이
M 이상 N 이하의 모든 소수를 구하면 됨.
그런데 M, N이 최대 100만 까지 가능하므로 O(N^2) 으로는 1천억이 되어 해결 불가.
그래서 빠른 방법을 사용해야 함.

에라토스테네스의 체를 사용하면 특정 범위의 모든 소수를 O(N log log N) 에 빠르게 구할 수 있다.
"""
import math

M, N = map(int, input().split())
arr = [True] * (N + 1)
# 1은 소수가 아니므로 제외
arr[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i]:
        for j in range(i * 2, N + 1, i):
            arr[j] = False

for i in range(M, N + 1):
    if arr[i]:
        print(i)
