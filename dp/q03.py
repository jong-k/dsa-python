"""
p.223 바닥 공사
백준 2*n 타일링
"""

"""풀이
dp(1) = 1
dp(2) = 3
dp(3) 을 살펴보면 아래 3가지 경우의 수로 나눌 수 있음
1 2 3
| dp(2) => 처음엔 2*1 타일 깔고 남은 공간은 dp(2) => 3
ㅁ dp(1) => 처음엔 2*2 타일 깔고 남은 공간은 dp(1) => 1
= dp(1) => 처음엔 1*2 타일 스택으로 깔고 남은 공간은 dp(1) => 1

dp(3) = 3 + 2 * 1 = 5

dp(4) 도 아래 3가지 경우의 수로 나눌 수 있음
1 2 3 4
| dp(3) => 5
ㅁ dp(2) => 3
= dp(2) => 3

dp(5) = 5 + 2 * 3 = 11

점화식
dp(n) = dp(n-1) + 2 * dp(n-2)
"""


def solution(n):
    memo = [0] * 1001
    memo[1] = 1
    memo[2] = 3
    for i in range(3, n + 1):
        memo[i] = (memo[i - 1] + 2 * memo[i - 2]) % 796796
    return memo[n]


print(solution(3))  # 5
