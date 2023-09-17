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
visited = [False] * (node_num + 1)
distance = [INF] * (node_num + 1)

# 방향 그래프 준비
for _ in range(edge_num):
    start, end, cost = map(int, input_data[_ + 2].split())
    graph[start].append((end, cost))


def get_smallest_node():
    """
    미방문 노드중에서 가장 최단 거리가 짧은 노드 번호 반환
    :return: 노드 번호
    """
    min_value = INF
    node_index = 0
    for i in range(1, node_num + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            node_index = i
    return node_index


def dijkstra(start):
    """
    다익스트라 알고리즘으로 distance 리스트 완성
    :param start: 시작 노드
    """
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for tup in graph[start]:
        distance[tup[0]] = tup[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(node_num - 1):
        # 현재 가장 최단거리 짧은 노드 꺼내서 방문처리
        current_node = get_smallest_node()
        visited[current_node] = True
        # 현재 노드에 연결된 다른 노드 확인
        for neighbor in graph[current_node]:
            new_cost = distance[current_node] + neighbor[1]
            if cost < distance[neighbor[0]]:
                distance[neighbor[0]] = new_cost


# 다익스트라 알고리즘 수행
dijkstra(start_node)
print(distance[1:])
