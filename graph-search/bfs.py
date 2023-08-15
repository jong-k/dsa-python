from collections import deque

# 메모리를 적게 차지하는 인접 리스트 사용
Graph = [
    [],  # 인덱스 계산 편의상 0번 노드는 없다고 가정
    [2, 3, 8],  # 1번 노드의 인접 노드 리스트
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 방문 리스트
Visited = [False] * 9


def bfs(graph, start_node, visited):
    """
    :param graph: 인접 리스트 (2차원 리스트)
    :param start_node: 시작 노드 번호 (자연수)
    :param visited: 각 노드별 방문 여부 (리스트)
    :return: 그래프 순회 경로 (리스트)
    """
    queue = deque([start_node])
    visited[start_node] = True
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor_node in graph[node]:
            if not visited[neighbor_node]:
                queue.append(neighbor_node)
                visited[neighbor_node] = True
    return result


print(bfs(Graph, 1, Visited))  # [1, 2, 3, 8, 7, 4, 5, 6]
