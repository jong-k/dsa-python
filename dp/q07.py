"""
p.377 퇴사
백준 14501
"""

"""풀이
뒤에서부터 계산하면 편하다
"""
days = int(input())
period_list = []
price_list = []
# memo[i] = i번째 날부터 마지막 날까지의 최대 금액
memo = [0] * (days + 1)
max_value = 0

for _ in range(days):
    period, price = map(int, input().split())
    period_list.append(period)
    price_list.append(price)

# i = period_list, price_list의 마지막 인덱스부터 시작
for i in range(days - 1, -1, -1):
    # 막날 1일 걸리면 돈 받을 수 있음
    end_day = i + period_list[i]
    # 상담 가능하면
    if end_day <= days:
        # memo[end_day] = 0 부터 시작함
        # memo[i + 1] = 0
        # i번째 날부터 마지막 날까지 벌 수 있는 최대 금액은
        # i의 end day 금액: memo[end_day] + i 금액 과
        # i번째 날을 선택하지 않았을 때 이전 날 금액: memo[i + 1] 을 비교
        memo[i] = max(price_list[i] + memo[end_day], memo[i + 1])
        # 최댓값이 존재하면 최신화해줌
        max_value = memo[i]
    else:
        memo[i] = max_value

print(max_value)
