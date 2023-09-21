from heapq import heappop, heappush

input_data = ("6 11\n"
              "1\n"
              "1 2 2\n"
              "1 3 5\n"
              "1 4 1\n"
              "2 3 3\n"
              "2 4 2\n"
              "3 2 3\n"
              "3 6 5\n"
              "4 3 3\n"
              "4 5 1\n"
              "5 3 1\n"
              "5 6 2")

INF = int(1e9)
input_data = input_data.split("\n")
node_num, edge_num = map(int, input_data[0].split())
start_node = int(input_data[1])
graph = [[] for _ in range(node_num + 1)]
distance = [INF] * (node_num + 1)

# 방향 그래프 준비
for _ in range(edge_num):
    start, end, cost = map(int, input_data[_ + 2].split())
    graph[start].append((end, cost))

"""그래프
[
  [], -> 계산 편하게 하기 위한 미사용 
  [(2, 2), (3, 5), (4, 1)], -> 1번 노드
  [(3, 3), (4, 2)],
  [(2, 3), (6, 5)],
  [(3, 3), (5, 1)],
  [(3, 1), (6, 2)],
  [] -> 마지막 노드
]
"""


def dijkstra(start):
    pq = []
    # 시작 노드의 최단 경로는 0
    heappush(pq, (start, 0))
    distance[start] = 0
    while pq:
        # 가장 최단거리가 짧은 노드 정보 꺼내기
        current_node, cost = heappop(pq)
        # 현재 노드까지의 거리가 INF보다 작으면 이미 방문된 것이므로 스킵
        if distance[current_node] < cost:
            continue
        # 인접 노드 확인
        for neighbor in graph[current_node]:
            new_cost = distance[current_node] + neighbor[1]
            if new_cost < distance[neighbor[0]]:
                distance[neighbor[0]] = new_cost
                heappush(pq, (neighbor[0], new_cost))


dijkstra(start_node)
# 노드 1번에서 각 노드까지의 최단 거리
print(distance[1:])  # [0, 2, 3, 1, 2, 4]
