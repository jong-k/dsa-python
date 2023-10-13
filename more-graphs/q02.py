"""
p.300 도시 분할 계획
백준 1647
"""

"""풀이
마을을 2개로 분리 => 2개의 최소 신장 트리 만들기
일단 최소 신장 트리를 만들고, 그 중에서 가장 비용이 높은 간선을 제거하면 자동으로 2개의 최소 신장 트리를 만들 수 있ㄷ 
"""
import sys


def find_root(root_list, node):
    if root_list[node] != node:
        return find_root(root_list, root_list[node])
    return root_list[node]


def union_root(root_list, node1, node2):
    root_node1 = find_root(root_list, node1)
    root_node2 = find_root(root_list, node2)
    if root_node1 < root_node2:
        root_list[root_node2] = root_node1
    else:
        root_list[root_node1] = root_node2


house_num, road_num = map(int, sys.stdin.readline().split())
root_arr = [x for x in range(0, house_num + 1)]
total_cost = 0
max_cost = 0
road_arr = []

for _ in range(road_num):
    house1, house2, cost = map(int, sys.stdin.readline().split())
    road_arr.append((house1, house2, cost))

road_arr.sort(key=lambda x: x[2])

for house1, house2, cost in road_arr:
    if find_root(root_arr, house1) != find_root(root_arr, house2):
        union_root(root_arr, house1, house2)
        total_cost += cost
        max_cost = max(max_cost, cost)

print(total_cost - max_cost)
