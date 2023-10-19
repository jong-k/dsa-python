"""
p.399 최종 순위
백준 3665
"""

"""풀이
인접 리스트 대신 인접 행렬을 사용하는게 편리함
-> 5 4 3 2 1 순으로 방향 그래프를 만들고, 순위 변동이 있는 경우, 방향 그래프를 업데이트해줘야 하기 때문
-> 방향 그래프 업데이트 시 간선을 바꿔야 하기 때문에 O(1)에 변경 가능한 인접 행렬이 유리
-> 또한 바뀐 순위가 2 4, 3 4 형태로 주어지기 때문에 고유한 간선으로 표시 불가!
"""
import sys
from collections import deque


def topology_sort(nodes, indegrees, graph):
    result = []
    queue = deque()

    for i in range(1, nodes + 1):
        if indegrees[i] == 0:
            queue.append(i)

    for i in range(nodes):
        # 큐가 비면 사이클이 발생 (성립할 수 없는 경우)
        if len(queue) == 0:
            return "IMPOSSIBLE"
        # 큐에 원소가 2개 이상 존재하면 답이 여러개일 수 있음
        if len(queue) >= 2:
            return "IMPOSSIBLE"
        current_node = queue.popleft()
        result.append(current_node)

        for next_node in range(1, nodes + 1):
            # 연결된 노드에 대해서 진입차수 -1
            if graph[current_node][next_node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    queue.append(next_node)

    return " ".join(map(str, result))


case_num = int(sys.stdin.readline())
for _ in range(case_num):
    node_num = int(sys.stdin.readline())
    indegree_list = [0] * (node_num + 1)
    adjacent_matrix = [[False] * (node_num + 1) for _ in range(node_num + 1)]
    old_order = list(map(int, sys.stdin.readline().split()))
    # 일자 형태의 그래프가 아닌 맨 처음 노드는 자기 보다 후순위 노드에 방향, 맨 마지막 노드는 받는 방향이 없는 형태의 그래프
    # 인접 행렬의 row는 시작 노드, col은 도착 노드
    for i in range(node_num):
        for j in range(i + 1, node_num):
            start = old_order[i]
            end = old_order[j]
            adjacent_matrix[start][end] = True
            indegree_list[end] += 1

    change_num = int(sys.stdin.readline())

    for _ in range(change_num):
        start, end = map(int, sys.stdin.readline().split())
        # 바뀐 순위를 그래프에 업데이트
        if adjacent_matrix[start][end]:
            adjacent_matrix[start][end] = False
            adjacent_matrix[end][start] = True
            indegree_list[start] += 1
            indegree_list[end] -= 1
        else:
            adjacent_matrix[start][end] = True
            adjacent_matrix[end][start] = False
            indegree_list[start] -= 1
            indegree_list[end] += 1

    print(topology_sort(node_num, indegree_list, adjacent_matrix))
