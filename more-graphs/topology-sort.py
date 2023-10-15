from collections import deque

input1 = ("7 8\n"
          "1 2\n"
          "1 5\n"
          "2 3\n"
          "2 6\n"
          "3 4\n"
          "4 7\n"
          "5 6\n"
          "6 4")

data = input1.split("\n")
vertex_num, edge_num = map(int, data[0].split())
# 모든 노드에 대한 진입 차수를 0으로 초기화
indegree_list = [0] * (vertex_num + 1)
# 방향 그래프
graph = [[] for _ in range(vertex_num + 1)]

# 간선 데이터 입력받아 그래프 완성
for i in range(edge_num):
    start, end = map(int, data[i + 1].split())
    graph[start].append(end)
    indegree_list[end] += 1  # 진입 차수 업데이트

# 완성된 그래프
"""각 인덱스에 이동 가능한 정점을 원소로 가짐
graph = [
    [],
    [2, 5],
    [3, 6],
    [4],
    [7],
    [6],
    [4],
    []
    ]
"""


def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result = []
    queue = deque()

    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, vertex_num + 1):
        if indegree_list[i] == 0:
            queue.append(i)

    while queue:
        current_node = queue.popleft()
        result.append(current_node)
        for next_node in graph[current_node]:
            # 해당 노드와 연결된 노드들의 진입 차수 -1 처리
            indegree_list[next_node] -= 1
            # 진입 차수가 0이 되면 큐에 삽입
            if indegree_list[next_node] == 0:
                queue.append(next_node)

    return result


print(topology_sort())  # [1, 2, 5, 3, 6, 4, 7]
