"""
p.395 탑승구
"""

"""풀이
유니언 파인드를 활용한다

탑승구 숫자가 4개 이면 아래의 노드 배열로 시작한다
그리고 루트 노드가 0인 순간, 더 이상 도킹할 수 없다고 본다
0 1 2 3 4

도킹 횟수를 기록할 answer 변수 사용

비행기 배열이 2 2 3 3 4 4 라면

1. 비행기 2
도킹 가능한 가장 큰 탑승구부터 도킹한다
여기서 도킹을 union 연산이라고 보면, 

0 1-2 3 4 형태가 된다
도킹 횟수 1

2. 비행기 2
1-2 유니언이 발생했으니 1-0 유니언을 실행해야 하는데,
비행기 2의 루트노드는 자연스럽게 1이므로, (root, root - 1) 끼리 유니언 연산을 수행하면 된다

0-1-2 3 4 형태가 된다
도킹 횟수 2

3. 비행기 3
비행기 3의 루트는 3이다 (초기값)

0-1-2-3 4 형태가 된다
도킹 횟수 3

4. 비행기 3
비행기 3의 루트가 0이므로 순회를 종료한다
도킹 횟수 3 출력
"""

input1 = ("4\n"
          "3\n"
          "4\n"
          "1\n"
          "1")
# 2

input2 = ("4\n"
          "6\n"
          "2\n"
          "2\n"
          "3\n"
          "3\n"
          "4\n"
          "4")
# 3

data = list(map(int, input2.split("\n")))

gate_num = data[0]
plane_num = data[1]
root_arr = [x for x in range(gate_num + 1)]
answer = 0


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


for plane in data[2:]:
    root = find_root(root_arr, plane)
    # 루트 노드가 0이면 잔여 공간이 없는 것으로 인식
    if root == 0:
        break
    union_root(root_arr, root, root - 1)
    answer += 1

print(answer)  # 3
