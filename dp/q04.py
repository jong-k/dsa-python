"""
p.226 효율적인 화폐 구성
백준 2294 동전 2
"""

"""풀이
DP를 어떻게 적용할까?
일단 구해야 하는 것은 최소 사용 화폐 갯수
그럼 매 금액을 만들어가면서 최소 사용 화폐 갯수를 최적화해나가면 된다

예) 2 15
2
3

dp(15) = min( dp(13) + 1, dp(12) + 1 )
ㄴ dp(13) = min( dp(11) + 1, dp(10) + 1 )
ㄴ dp(12) = min( dp(10) + 1, dp(9) + 1 )
ㄴㄴ dp(11) = min( dp(9) + 1, dp(8) + 1 )
ㄴㄴ  dp(10) = min( dp(8) + 1, dp(7) + 1 )
ㄴㄴ  dp(9) = min( dp(7) + 1, dp(6) + 1 )
ㄴㄴㄴ dp(8) = min( dp(6) + 1, dp(5) + 1 )
ㄴㄴㄴ dp(7) = min( dp(5) + 1, dp(4) + 1 )
ㄴㄴㄴ dp(6) = min( dp(4) + 1, dp(3) + 1 )
ㄴㄴㄴㄴ dp(5) = min( dp(3) + 1, dp(2) + 1 )
ㄴㄴㄴㄴ dp(4) = min( dp(2) + 1, dp(1) + 1 )
기본 dp(3) = 1
기본 dp(2) = 1


...

dp(15)를 만들기 위해 dp(1) 부터 만들어나가보자 (상향식)
"""

input1 = ("2 15\n"
          "2\n"
          "3")

input2 = ("3 4\n"
          "3\n"
          "5\n"
          "7")


def solution(data):
    data = data.split("\n")
    money_category_num, target_money = map(int, data.pop(0).split())
    money_list = list(map(int, data))
    memo = [-1] * 10001
    for money in money_list:
        memo[money] = 1

    for i in range(1, target_money):
        if memo[i] >= 1:
            for money in money_list:
                # 한번도 기록되지 않은 금액이면 +1 해주고
                # 기록된 적이 있으면 최솟값 따짐
                memo[i + money] = memo[i] + 1 if memo[i + money] == -1 else min(memo[i + money], memo[i] + 1)
    return memo[target_money]


print(solution(input1))  # 5
print(solution(input2))  # -1
