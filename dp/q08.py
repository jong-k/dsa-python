"""
p.380 병사 배치하기
백준 18353
"""

"""풀이
LIS(최장 증가 부분 수열) 을 활용한다

"""
soldier_num = int(input())
soldier_list = list(map(int, input().split()))
# memo 배열에 맨 처음부터 해당 인덱스까지의 최장 증가 부분수열 갯수를 저장
# e.g. memo[5] : 인덱스 0부터 5까지의 최장 증가 부분 수열 갯수
# 최소 1이므로 1로 초기화
memo = [1] * soldier_num
# 인덱스 0부터 1 ~ 마지막 원소 까지의 LIS 갯수를 계산
for i in range(1, soldier_num):
    # 시작은 맨 앞부터이므로 j = 0 고정 시작
    for j in range(i):
        # 내림차순을 만족하면, 즉 (맨 처음부터) 현재항 > (고정) 기준항
        if soldier_list[j] > soldier_list[i]:
            # LIS 갯수를 초기값 1부터 1씩 증가
            # 내림차순 끊겨도 이전 최댓값을 보존
            memo[i] = max(memo[i], memo[j] + 1)

# 최종 memo = [1, 2, 3, 3, 4, 5, 5]
print(soldier_num - max(memo))
