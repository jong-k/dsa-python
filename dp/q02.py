"""
p.220 개미 전사
"""

"""풀이
패턴을 찾아 점화식을 세우자

list = [6 1 2 6] 이라고 할 때

dp(1) = li[0] => 6
dp(2) = max(dp(1), li[1]) => max(6, 1) => 6
dp(3) = max(dp(2), dp(1) + li[2]) => max(6, 8) => 8
dp(4) = max(dp(3), dp(2) + li[3]) => max(8, 12) => 12
"""

input1 = ("4\n"
          "1 3 1 5")

input2 = ("4\n"
          "6 3 1 7")


def solution(data):
    data = data.split("\n")
    depot_size = int(data[0])
    depot_list = list(map(int, data[1].split()))

    memo = [0] * (depot_size + 1)
    memo[1] = depot_list[0]
    memo[2] = max(depot_list[0], depot_list[1])
    for i in range(3, depot_size + 1):
        memo[i] = max(memo[i - 1], memo[i - 2] + depot_list[i - 1])
    return memo[depot_size]


print(solution(input1))  # 8
print(solution(input2))  # 13
