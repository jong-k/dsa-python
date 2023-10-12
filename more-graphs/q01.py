"""
p.298 팀 결성
"""

input1 = ("7 8\n"
          "0 1 3\n"
          "1 1 7\n"
          "0 7 6\n"
          "1 7 1\n"
          "0 3 7\n"
          "0 4 2\n"
          "0 1 1\n"
          "1 1 1")


def find_root(root, x):
    if root[x] != x:
        return find_root(root, root[x])
    return root[x]


def union_root(root, node1, node2):
    root_node1 = find_root(root, node1)
    root_node2 = find_root(root, node2)
    if root_node1 < root_node2:
        root[root_node2] = root_node1
    else:
        root[root_node1] = root_node2


data = input1.split("\n")
vertex_num, case_num = map(int, data[0].split())
root_list = [x for x in range(0, vertex_num + 1)]

for i in range(1, case_num + 1):
    is_find, node1, node2 = map(int, data[i].split())
    if is_find:
        if find_root(root_list, node1) == find_root(root_list, node2):
            print("YES")
        else:
            print("NO")
    else:
        union_root(root_list, node1, node2)
