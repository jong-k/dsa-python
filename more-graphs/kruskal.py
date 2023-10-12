vertex_num = 7
edge_num = 9
edges = [(1, 2, 29), (1, 5, 75), (2, 3, 35), (2, 6, 34), (3, 4, 7), (4, 6, 23), (4, 7, 13), (5, 6, 53), (6, 7, 25)]
root_list = [x for x in range(vertex_num + 1)]
total_cost = 0  # 최종 비용


def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    # return x # 원래 방법
    return root[x]  # 경로 압축 : 바로 루트 노드에 접근하는, 더 효율적인 방법


def union_root(root, node1, node2):
    root_node1 = find_root(root, node1)
    root_node2 = find_root(root, node2)
    if root_node1 < root_node2:
        root[root_node2] = root_node1
    else:
        root[root_node1] = root_node2


edges.sort(key=lambda x: x[2])  # 비용 기준 오름차순 정렬

for start, end, cost in edges:
    # 사이클이 발생하지 않는 간선만 집합에 포함
    # 루트 노드가 같으면 사이클이 발생한 것으로 봄
    if find_root(root_list, start) != find_root(root_list, end):
        union_root(root_list, start, end)
        total_cost += cost

print(total_cost)  # 159
