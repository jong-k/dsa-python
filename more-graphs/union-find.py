vertex_num = 6
edge_num = 4
union_data = [(1, 4), (2, 3), (2, 4), (5, 6)]
# 부모노드 테이블 초기화
parent = [x for x in range(vertex_num + 1)]


# find 함수
def find_parent(parent, node):
    """
    특정 노드의 루트 노드 반환
    :param parent: 부모 테이블 (1차원 리스트)
    :param node: 루트 노드를 찾을 원소 (number)
    :return: 루트 노드 번호
    """
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀 호출
    if parent[node] != node:
        return find_parent(parent, parent[node])
    # return node
    return parent[node]  # 경로 압축으로 최적화


# union 함수
def union_parent(parent, node1, node2):
    """
    두 노드의 루트 노드를 같게 함
    :param parent: 부모 테이블
    :param node1: 노드1
    :param node2: 노드2
    """""
    root_node1 = find_parent(parent, node1)
    root_node2 = find_parent(parent, node2)
    if root_node1 < root_node2:
        parent[root_node2] = root_node1
    else:
        parent[root_node1] = root_node2


# union 연산 수행
for a, b in union_data:
    union_parent(parent, a, b)

# 부모 테이블
print(parent)  # [0, 1, 1, 2, 1, 5, 5]

# 루트 노드 반환
for i in range(1, vertex_num + 1):
    print("노드 번호:{} 루트 노드:{}".format(i, find_parent(parent, i)))

"""
노드 번호:1 루트 노드:1
노드 번호:2 루트 노드:1
노드 번호:3 루트 노드:1
노드 번호:4 루트 노드:1
노드 번호:5 루트 노드:5
노드 번호:6 루트 노드:5
"""
