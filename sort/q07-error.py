"""
p.363 카드 정렬하기
백준 1715
"""
import sys
from collections import deque

card_list = []
answer = 0
card_num = int(sys.stdin.readline())
for _ in range(card_num):
    card_list.append(int(sys.stdin.readline()))
card_list_queue = deque(sorted(card_list))

while card_list_queue:
    if len(card_list_queue) == 1:
        answer += card_list_queue.popleft()
        break
    else:
        first = card_list_queue.popleft()
        second = card_list_queue.popleft()
        answer += first + second
        if len(card_list_queue) > 0:
            card_list_queue.appendleft(first + second)
        else:
            break
print(answer)

"""틀린 이유
10 20 40 이면
answer += 10
answer += 20

30 40
answer += 30
answer += 40

answer = 100 으로 가능하지만,

70 80 90 100 인 경우
answer += 70
answer += 80

150 90 100 이 되어버리므로 이 때는 
answer += 90
answer += 100 을 먼저 수행해야 함

매번 정렬을 시행하면 시간이 많이 걸리므로..
우선순위 큐를 활용하여 빠르게 최솟값을 pop 할 수 있어야 함
"""
