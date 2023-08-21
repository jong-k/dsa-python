"""
p.363 카드 정렬하기
백준 1715
"""
import sys
import heapq  # PriorityQueue 보다 속도가 빠른 heapq 사용

card_list = []
answer = 0
card_num = int(sys.stdin.readline())
for _ in range(card_num):
    card_list.append(int(sys.stdin.readline()))

# N == 1 이면 비교횟수가 0이므로 바로 종료
if card_num == 1:
    print(0)
    sys.exit()

# card_list를 최소 힙으로 변환
heapq.heapify(card_list)

while card_list:
    if len(card_list) == 1:
        answer += heapq.heappop(card_list)
        break
    else:
        first = heapq.heappop(card_list)
        second = heapq.heappop(card_list)
        answer += first + second
        if len(card_list) > 0:
            heapq.heappush(card_list, first + second)
        else:
            break
print(answer)
