"""
p.397 어두운 길
백준 6497 전력난
"""

import sys

answers = []


def find_root(roots, node):
    if roots[node] != node:
        return find_root(roots, roots[node])
    return roots[node]


def union_root(roots, node1, node2):
    root1 = find_root(roots, node1)
    root2 = find_root(roots, node2)
    if root1 < root2:
        roots[root2] = root1
    else:
        roots[root1] = root2


def solution(nodes, edges):
    edge_list = []

    for _ in range(edges):
        edge_list.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

    edge_list.sort(key=lambda x: x[2])

    root_list = [x for x in range(nodes)]
    saved_cost = 0

    for start, end, cost in edge_list:
        if find_root(root_list, start) != find_root(root_list, end):
            union_root(root_list, start, end)
        else:
            saved_cost += cost

    return saved_cost


while True:
    node_num, edge_num = map(int, sys.stdin.readline().split())
    if node_num == edge_num == 0:
        for answer in answers:
            print(answer)
        break

    answers.append(solution(node_num, edge_num))
