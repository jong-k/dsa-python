"""
p.262 전보
"""

"""풀이
- 방향 그래프
- C에서 출발해 각기 다른 지점까지 연결된 경로의 갯수 및 가장 오래 걸린 시간
=> 다익스트라
"""
from heapq import heappop, heappush

input1 = ("3 2 1\n"
          "1 2 4\n"
          "1 3 2")


def solution(input_data):
    INF = int(1e9)
    input_data = input_data.split("\n")
    node_num, edge_num, departure = map(int, input_data[0].split())
    graph = [[] for _ in range(node_num + 1)]
    distance = [INF] * (node_num + 1)
    distance[departure] = 0
    pq = []
    heappush(pq, (departure, 0))
    # 방향 그래프를 입력값으로 초기화
    for i in range(1, edge_num + 1):
        start, end, value = map(int, input_data[i].split())
        graph[start].append((end, value))

    while pq:
        current_node, cost = heappop(pq)
        # 방문 이력있으면 무시
        if distance[current_node] < cost:
            continue

        for neighbor in graph[current_node]:
            new_node = neighbor[0]
            new_cost = distance[current_node] + neighbor[1]
            # 새로 방문할 노드의 기존 거리가 현재 노드 + 방문할 노드의 거리보다 크면 업데이트
            if new_cost < distance[new_node]:
                distance[new_node] = new_cost
                heappush(pq, (neighbor[0], new_cost))

    connected_num, max_distance = 0, 0
    for i in range(1, node_num + 1):
        if distance[i] < INF:
            connected_num += 1
            max_distance = max(max_distance, distance[i])

    print(connected_num - 1, max_distance)


solution(input1)  # 2 4
