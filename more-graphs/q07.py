"""
p.398 행성 터널
백준 2887
"""

"""풀이
N개의 모든 행성이 N-1개의 터널로 연결된다 => 최소 신장 트리
3차원 좌표간 최소 비용을 기준으로 간선 정보 정렬하는 방법 => 그냥 정렬해보기? => 불가능 (시간 너무 많이 걸림 5C2)
대신 문제에서 거리를 구하기 위해 아래 조건을 제시함을 이용

문제 이해를 위해 만든 함수 : 2개의 (x,y,z) 를 비교하여 절댓값이 가장 작은 (x,y,z) 중 1개를 거리로 채택
def calc_cost(pos1, pos2):
    return min(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]), abs(pos1[2] - pos2[2]))

=> 이를 통해 x 끼리, y 끼리, z 끼리 중에서 최소인것들을 구하고, 이후 노드 번호가 중복되면 자동으로 union 하지 않으며 이 때의 행성간 거리를 더해주면 됨
"""
import sys


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


node_num = int(sys.stdin.readline())
root_list = [x for x in range(node_num + 1)]
edge_list = []
total_cost = 0
x_list = []
y_list = []
z_list = []

for node in range(1, node_num + 1):
    x, y, z = map(int, sys.stdin.readline().split())
    x_list.append((x, node))
    y_list.append((y, node))
    z_list.append((z, node))

x_list.sort()
y_list.sort()
z_list.sort()

# 간선 정보 튜플 (x1~x2 부터 z1~z2 까지의 거리, 시작점, 끝점) 형태 를 모두 간선 정보 배열에 넣음
# 이 배열을 거리 기준 정렬하고 최소 신장 트리 알고리즘 수행 => 1행성 x 거리, y거리, z거리 들 중에서 거리 적은 순으로 먼저 실행되므로
# => 나중에 수행된 것들은 이미 동일 루트이므로 유니언 연산 실행되지 않음! => 이를 통해 행성1~행성2 간 최소 x,y,z 거리만 적용할 수 있음
for i in range(node_num - 1):
    edge_list.append((x_list[i + 1][0] - x_list[i][0], x_list[i][1], x_list[i + 1][1]))
    edge_list.append((y_list[i + 1][0] - y_list[i][0], y_list[i][1], y_list[i + 1][1]))
    edge_list.append((z_list[i + 1][0] - z_list[i][0], z_list[i][1], z_list[i + 1][1]))

edge_list.sort()

for cost, start, end in edge_list:
    if find_root(root_list, start) != find_root(root_list, end):
        union_root(root_list, start, end)
        total_cost += cost

print(total_cost)
