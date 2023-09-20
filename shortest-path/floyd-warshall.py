INF = int(1e9)  # 10억

node_number = 4
edge_number = 7
# 출발, 도착, 거리 가 담긴 간선 데이터
data = ["1 2 4", "1 4 6", "2 1 3", "2 3 7", "3 1 5", "3 4 4", "4 3 2"]

graph = [[INF] * (node_number + 1) for _ in range(node_number + 1)]

# 자기 자신으로 가는 거리 0으로 초기화
for i in range(1, node_number + 1):
    graph[i][i] = 0

# 간선 정보 업데이트
for edge_info in data:
    start, end, distance = map(int, edge_info.split())
    graph[start][end] = distance

print("기존 배열")
for i in range(1, node_number + 1):
    for j in range(1, node_number + 1):
        val = graph[i][j] if graph[i][j] < INF else "INF"
        print(val, end=" ")
    print()

# 플로이드 워셜 알고리즘 수행
for i in range(1, node_number + 1):
    for j in range(1, node_number + 1):
        for k in range(1, node_number + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

print("변경된 배열")
for i in range(1, node_number + 1):
    for j in range(1, node_number + 1):
        print(graph[i][j], end=" ")
    print()

"""
기존 배열
0 4 INF 6 
3 0 7 INF 
5 INF 0 4 
INF INF 2 0 
변경된 배열
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 
"""
