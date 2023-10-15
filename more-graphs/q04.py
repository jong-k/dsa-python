"""
p.393 여행 계획
"""

"""풀이
예를 들어 2 -> 3 -> 4 -> 3 경로가 가능한지 테스트하려면,
2,3 연결 확인
3,4 연결 확인
4,3 연결 확인이 필요하다

이 때 연결은 유니온 파인드의 find 연산으로 생각할 수 있다
인접 행렬을 받아서 간선 정보 추출 가능
"""

input1 = ("5 4\n"
          "0 1 0 1 1\n"
          "1 0 1 1 0\n"
          "0 1 0 0 0\n"
          "1 1 0 0 0\n"
          "1 0 0 0 0\n"
          "2 3 4 3")

data = input1.split("\n")
vertex_num, travel_node_num = map(int, data[0].split())
adjacent_matrix = []
edge_list = []
root_list = [x for x in range(vertex_num + 1)]
# 여행 경로
travel_path = list(map(int, data[-1].split()))

# 인접 행렬 초기화
for i in range(1, vertex_num + 1):
    adjacent_matrix.append(list(map(int, data[i].split())))

# 간선 정보 만들기
for i in range(vertex_num):
    for j in range(i + 1, vertex_num):
        if adjacent_matrix[i][j] == 1:
            edge_list.append((i + 1, j + 1))


def find_root(root_arr, node):
    if root_arr[node] != node:
        root_arr[node] = find_root(root_arr, root_arr[node])
    return root_arr[node]


def union_root(root_arr, node1, node2):
    root_node1 = find_root(root_arr, node1)
    root_node2 = find_root(root_arr, node2)
    if root_node1 < root_node2:
        root_arr[root_node2] = root_node1
    else:
        root_arr[root_node1] = root_node2


# 간선 순회하며 root_list 업데이트
for start, end in edge_list:
    if find_root(root_list, start) != find_root(root_list, end):
        union_root(root_list, start, end)

# 여행 경로 순회
for i in range(travel_node_num - 1):
    if find_root(root_list, travel_path[i]) != find_root(root_list, travel_path[i + 1]):
        print("NO")
        break

print("YES")
