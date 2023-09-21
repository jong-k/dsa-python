"""
p.259 미래 도시
"""

"""풀이
- 무방향 그래프
- 모든 간선의 거리는 1
- 시작 -> K -> 도착 => 플로이드 워셜
"""

input1 = ("5 7\n"
          "1 2\n"
          "1 3\n"
          "1 4\n"
          "2 4\n"
          "3 4\n"
          "3 5\n"
          "4 5\n"
          "4 5")

input2 = ("4 2\n"
          "1 3\n"
          "2 4\n"
          "3 4")


def solution(input_data):
    input_data = input_data.split("\n")
    node_num, edge_num = map(int, input_data[0].split())
    # 1에서 middle을 거쳐 destination까지 가는 최단 경로 구하기
    # 1 -> 5 -> 4
    #    4         5
    destination, middle = map(int, input_data[-1].split())
    INF = int(1e9)
    graph = [[INF] * (node_num + 1) for _ in range(node_num + 1)]

    for i in range(1, node_num + 1):
        graph[i][i] = 0

    for i in range(1, edge_num + 1):
        start, end = map(int, input_data[i].split())
        graph[start][end] = 1
        graph[end][start] = 1

    for i in range(1, node_num + 1):
        for j in range(1, node_num + 1):
            for k in range(1, node_num + 1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

    distance = graph[1][middle] + graph[middle][destination]
    if distance >= INF:
        print(-1)
    else:
        print(distance)


solution(input1)  # 3
solution(input2)  # -1
