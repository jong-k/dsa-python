"""
p.316 무지의 먹방 라이브
프로그래머스 lv4
스택 사용 버전 -> 우선순위 큐보다 효율성 테스트에서 살짝 느리나 올 패스
"""

"""풀이
food_times의 length가 최대 1억에 육박하므로 O(N^2)로는 1억의 제곱이 되어 해결 불가
O(N * logN) 으로는 8억 정도는 되므로 해결 가능하다

아이디어 : 먹는 시간이 적은 음식 순으로 먼저 제거해나간다 (그리디 -> 먹는 시간이 오래 걸릴 수록 마지막까지 남아있을 것이므로)

"""


def solution(food_times, k):
    # 다음에 먹을 음식이 없으면 -1
    if sum(food_times) <= k:
        return -1

    stack = []
    rest_time = k
    prev_food_time = 0
    current_food_number = len(food_times)

    for i in range(current_food_number):
        stack.append((food_times[i], i + 1))
    stack.sort(key=lambda x: x[0], reverse=True)  # 내림차순 정렬

    # 작업이 가능하면 반복
    # 반복문이 돌 때마다 이전에 빼준 값을 기억하고 빼줘야 함
    while rest_time >= (stack[current_food_number - 1][0] - prev_food_time) * current_food_number:
        # 가장 먹는 시간이 적은 음식을 우선순위 큐에서 pop
        current_food_time = stack.pop()[0]
        # 이전 먹는 시간을 빼줬으므로 현재 먹는 시간에서도 빼줌
        rest_time -= (current_food_time - prev_food_time) * current_food_number
        current_food_number -= 1
        prev_food_time = current_food_time

    # 더 이상 반복이 불가능할 정도로 남은 시간이라면 남은 우선순위 큐에서 정답 도출
    # 음식 번호 순으로 오름차순 정렬
    rest_food_times = sorted(stack, key=lambda x: x[1])
    # 다음 순서의 음식 번호 출력
    return rest_food_times[rest_time % current_food_number][1]


print(solution([8, 6, 4], 15))  # 2
print(solution([3, 1, 2], 5))  # 1
