# 최단 경로

## 목차

1. 문제 리스트
2. 기본 개념

## 1. 문제 리스트

1. 미래 도시
2. 전보
3. 플로이드
4. 정확한 순위
5. 화성 탐사
6. 숨바꼭질

## 2. 기본 개념

- 일반적으로 상황에 따른 가장 효율적인 알고리즘이 정립되어 있다
- 최단 경로 알고리즘에는 대표적으로 다익스트라, 플로이드 워셜, 벨만 포드 3가지가 있다
- 그리디 및 다이나믹 프로그래밍 개념이 최단 경로 알고리즘에 활용된다

### 2.1. 다익스트라 최단 경로 알고리즘

- 그래프에 여러 개의 노드가 있을 때, 특정한 노드에서 다른 노드까지의 각각의 최단 경로를 모두 구해주는 알고리즘
- 음의 간선(0보다 작은 값을 갖는 간선)이 없을 때 정상적으로 동작
  - 따라서 현실 세계를 반영할 수 있으므로 실제 GPS 소프트웨어들의 알고리즘으로 사용됨

#### 동작 원리

기본적으로 그리디 알고리즘에 속함 (매번 가장 비용이 적은 노드를 선택)

1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화
3. 미방문 노드중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3번과 4번을 반복

최단 거리 테이블 : 각 노드에 대한 현재까지의 최단 거리를 1차원 리스트에 저장한 것

#### 구현1 (간단한 버전)

- `naive-dijkstra.py`
- 시간복잡도 : O(V^2)
  - 각 노드를 순회하며 연결된 최단거리가 짧은 노드들을 선형 탐색하기 때문
  - 노드의 갯수가 10,000개를 넘을 경우 개선된 다익스트라 알고리즘이 필요

### 2.2. 개선된 다익스트라 알고리즘 (with 우선순위 큐)

- worst case에도 O(E logV) 에 해결 가능
- 기존 알고리즘은 최단 거리의 노드를 O(V)에 탐색했으나, 우선순위 큐를 사용하면 O(logV)에 탐색 가능

#### 우선순위 큐 (Priority Queue)

- 힙(Heap) : 스택, 큐와 다르게 우선순위가 높은 원소가 추출됨
- 파이썬에서는 `PriorityQueue` 와 `heapq` 라이브러리를 사용할 수 있음
  - 이 중, heapq가 더 빠르게 동작
  - 기본적으로 최소 힙으로 구현되어 있음

#### 동작 원리

- 우선순위 큐에서 꺼낸 노드에서 연결된 간선의 갯수(E)만큼 최단 거리 탐색(logE)
- 이 과정에서 우선순위 큐에 전체 간선들을 넣고 빼는 연산 실행 O(E logE)

#### 구현2 (리팩토링 버전)

- `refactored-dijkstra.py`
- 시간복잡도 : O(E logV)
  - N개의 데이터를 우선순위 큐로 빼내려면 O(N logN) 필요
  - 전체 간선은 E개 이므로 O(E logE) 가 된다
  - 이 때 중복 간선을 제거하면 E는 항상 V^2 보다 작다
  - 모든 정점이 연결되어 있다고 간선의 갯수는 V^2가 되기 때문
  - logV^2 = 2logV = logV 이므로 전체 시간복잡도는 `O(E logV)`

### 2.2. 플로이드 워셜 최단 경로 알고리즘

#### 다익스트라와 비교 1. 기능

- 플 : 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구할 때 사용
- 다 : 한 지점에서 다른 특정 지점까지의 최단 경로를 구할 때 사용

#### 비교 2. 관련 알고리즘

- 플 : DP
- 다 : 그리디

#### 비교 3. 동작 원리

- 플 : 모든 노드까지의 최단 거리를 저장하기 위해 2차원 리스트 활용
- 다 : 1차원 리스트 활용

#### 플로이드 워셜 동작 원리

1.방향 그래프를 준비한다

- row는 출발 노드, col은 도착 노드
- 연결되지 않는 간선은 무한(1e9) 입력
- 자기 자신과의 간선은 0 입력

2차원 방향 그래프

```
  1 2 3 4
1 0 4 I 6
2 3 0 7 I
3 5 I 0 4
4 I I 2 0
```

2.1번 노드를 거쳐가는 경우만 확인해보고 기존 경로와 비교해본다

- `memo[2][3]` 과 `2 -> 1 1 -> 3` 비교해서 최솟값 입력
- 2 -> 1 1 -> 4
- 3 -> 1 1 -> 2
- 3 -> 1 1 -> 4
- 4 -> 1 1 -> 2
- 4 -> 1 1 -> 3

이는 3P2 = 6 으로 표현할 수 있다

- 1을 제외한 3개 노드 중에 2개를 뽑아 나열하는 경우의 수 (순열)

업데이트된 2차원 방향 그래프

- memo[2][4], memo[3][2] 를 업데이트 시킴

```
  1 2 3 4
1 0 4 I 6
2 3 0 7 9
3 5 9 0 4
4 I I 2 0
```

3.마지막 4번 노드까지 이를 반복하면 최적화된 방향 그래프가 만들어진다

#### 구현

- `floyd-warshall.py`

#### 시간 복잡도

- O(N^3) : 노드의 갯수가 N개일 때 O(N^2)의 작업을 반복
