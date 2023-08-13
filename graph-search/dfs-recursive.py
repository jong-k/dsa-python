# 스택을 활용한 재귀 DFS 구현

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


def dfs_recursive(graph, start_node, visited, result):
    """
    :param graph: 인접 리스트 (2차원 리스트)
    :param start_node: 시작 노드 번호 (자연수)
    :param visited: # 각 노드별 방문 여부 (리스트)
    :param result: # 그래프 순회 경로 (리스트)
    :return: 그래프 순회 경로 (리스트)
    """
    visited[start_node] = True
    result.append(start_node)
    for neighbor_node in graph[start_node]:  # 최초 neighbor_node = 2
        if not visited[neighbor_node]:  # 미방문이면 방문해야 하므로
            dfs_recursive(graph, neighbor_node, visited, result)  # 이 미방문 노드를 시작으로 또 DFS 재귀 호출
    return result


print(dfs_recursive(Graph, 1, Visited, []))  # [1, 2, 7, 6, 8, 3, 4, 5]
