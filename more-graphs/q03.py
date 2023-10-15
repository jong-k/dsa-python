"""
p.303 커리큘럼
"""

"""풀이
모든 간선을 타면서 시간을 비교하기 위해 보관해야 함
-> 진입 차수가 0일 때 가장 오래 걸리는 시간을 최종 시간으로 채택하기 위해서
"""

from collections import deque

# 1행은 전체 노드 갯수
# 2행부터는 각 노드의 필요 시간, 필수 선행 노드 번호들, -1(끝을 알리는 표시)
input1 = ("5\n"
          "10 -1\n"
          "10 1 -1\n"
          "4 1 -1\n"
          "4 3 1 -1\n"
          "3 3 -1")

data = input1.split("\n")
vertex_num = int(data[0])
indegree_list = [0] * (vertex_num + 1)
graph = [[] for _ in range(vertex_num + 1)]
time_list = [0] * (vertex_num + 1)

for i in range(1, vertex_num + 1):
    info = list(map(int, data[i].split()))
    time_list[i] = info[0]
    for prev_node in info[1:-1]:
        indegree_list[i] += 1
        graph[prev_node].append(i)


def topology_sort():
    time_result = [[] for _ in range(vertex_num + 1)]
    # time_result 에 첫 출발 노드의 시간 초기화
    time_result[1].append(time_list[1])
    queue = deque()

    for node in range(1, vertex_num + 1):
        if indegree_list[node] == 0:
            queue.append(node)

    while queue:
        current_node = queue.popleft()
        # 가장 오래 걸리는 시간을 최종 시간으로 채택 (진입 차수가 0이 될 때 까지 모든 가능 경로를 비교해야하므로)
        time_result[current_node] = max(time_result[current_node])
        for next_node in graph[current_node]:
            indegree_list[next_node] -= 1
            # time_result 에 확정된 현재 노드의 시간 + 다음 노드의 시간을 보관
            time_result[next_node].append(time_result[current_node] + time_list[next_node])
            if indegree_list[next_node] == 0:
                queue.append(next_node)

    return time_result[1:]


print(topology_sort())  # [10, 20, 14, 18, 17]
