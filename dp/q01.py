"""
p.217 1로 만들기
백준 1463 1로 만들기
"""

"""풀이
1부터 N까지 바텀업 방식으로 연산횟수를 만들어나감

예) N = 4
가지 1개 당 1회의 연산

              dp(4)
          /         \
       dp(3)        dp(2)
     /   |            |
 dp(2)  dp(1)       dp(1)
/     
dp(1)
"""


def solution(n):
    # 각 인덱스에 필요 연산 횟수를 저장하는 리스트
    memo = [0] * (10 ^ 6 + 1)
    # 1 ~ n 까지 필요 연산 횟수 리스트를 작성해나감
    # 이때, 미리 연산된 값을 사용할 경우 최적화하게끔 코드 작성
    for i in range(2, n + 1):
        # 1을 빼는 경우
        memo[i] = memo[i - 1] + 1

        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i // 2] + 1)
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i // 3] + 1)
        if i % 5 == 0:
            memo[i] = min(memo[i], memo[i // 5] + 1)
    return memo[n]


print(solution(6))  # 2 (6 -> 3 -> 1 or 6 -> 2 -> 1)
