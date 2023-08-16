"""
p.339 특정 거리의 도시 찾기
백준 18352 실버2
"""
import sys
from collections import deque


def solution():
    # input() 보다 readline() 이 수행시간이 빠르다
    node_num, edge_num, distance_sum, start_node = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(node_num + 1)]
    # 각 노드까지의 거리를 저장하는 리스트
    distance_list = [0] * (node_num + 1)
    visited = [False] * (node_num + 1)
    visited[start_node] = True

    for _ in range(edge_num):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        graph[start].append(end)

    queue = deque([start_node])

    def bfs():
        result = []
        while queue:
            node = queue.popleft()
            if distance_list[node] == distance_sum:
                result.append(node)
                continue
            for i in graph[node]:
                if not visited[i]:
                    distance_list[i] = distance_list[node] + 1
                    queue.append(i)
                    visited[i] = True
        return result

    answer = sorted(bfs())
    if answer:
        for i in answer:
            print(i)
    else:
        print(-1)


solution()
