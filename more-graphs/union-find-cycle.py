# vertex_num = 3
# edge_num = 3
# edges = [(1, 2), (2, 3), (3, 1)]
# 사이클 발생

# vertex_num = 6
# edge_num = 4
# edges = [(1, 4), (2, 3), (2, 4), (5, 6)]
# 사이클 발생 False -> 5, 6이 따로 놈

vertex_num = 5
edge_num = 4
edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
# 사이클 발생 False

root_list = [x for x in range(vertex_num + 1)]


def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    return root[x]


def union_root(root, node1, node2):
    root_node1 = find_root(root, node1)
    root_node2 = find_root(root, node2)
    if root_node1 < root_node2:
        root[root_node2] = root_node1
    else:
        root[root_node1] = root_node2


# 사이클 발생 여부
isCycle = False

for a, b in edges:
    # 모든 간선을 순회하다가 루트 노드가 같으면 사이클이 발생한 것으로 봄
    if find_root(root_list, a) == find_root(root_list, b):
        isCycle = True
        break
    else:
        union_root(root_list, a, b)

print(isCycle)
