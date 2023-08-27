# 내장 함수
"""eval
수학 수식이 문자열 형태로 들어오면 해당 수식을 계산한 결과를 반환
"""
result = eval("1 + 2 * 10")
print(result)  # 21

# itertools : 반복되는 데이터 처리 라이브러리
"""permutations(순열)
iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산
permutations은 클래스이므로 리스트로 변환해서 사용할 수 있다
"""
from itertools import permutations, combinations, product, combinations_with_replacement

data = ["A", "B", "C"]
print(list(permutations(data, 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

"""combinations(조합)
iterable 객체에서 r개의 데이터를 뽑는 모든 경우를 계산
"""
print(list(combinations(data, 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

"""product(중복 순열)
iterable 객체에서 중복해서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산
"""
print(list(product(data, repeat=2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

"""combinations_with_replacement(중복 조합)
iterable 객체에서 중복해서 r개의 데이터를 뽑는 모든 경우를 계산
"""
print(list(combinations_with_replacement(data, 2)))

"""heapq : 우선순위 큐를 구현하기 위해 사용
PriorityQueue와 동일하지만, heapq가 속도가 더 빠르다
heapq는 최소 힙으로 구성되어 있어서 최상단의 원소를 빼는것만으로 O(nlogn)에 오름차순 정렬을 구현할 수 있다
"""
import heapq


def heapsort(iterable):  # 힙 정렬
    heap = []
    result = []
    for num in iterable:
        heapq.heappush(heap, num)
    for num in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 파이썬에서는 최대 힙을 제공하지 않기 때문에, heapq를 사용하여 최대 힙을 구현하려면
# 삽입 직전에 부호를 바꿔 저장하고 (-9, -8, ... )
# 힙에서 꺼낼 때 다시 원래 부호로 바꿔주면 된다

# 내림차순 정렬
def max_heapsort(iterable):
    max_heap = []
    result2 = []
    for num in iterable:
        heapq.heappush(max_heap, -num)  # 부호를 바꿔서 힙에 넣기 때문에 절댓값이 큰 수가 오히려 힙 최상단으로 간다
    for num in range(len(max_heap)):
        result2.append(heapq.heappop(max_heap) * -1)  # 꺼내며 다시 원래 부호로 바꿔줌
    return result2


print(max_heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

"""bisect : 이진 탐색 라이브러리
이진 탐색은 정렬된 배열에서 특정 원소를 찾아야 할 때 효과적이다
아래 메서드들은 모두 O(logn) 에 동작한다
bisect_left(a, x) : 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
bisect_right(a, x) : 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
"""
from bisect import bisect_left, bisect_right

list_a = [1, 2, 4, 4, 8]

print(bisect_left(list_a, 4))  # 2
print(bisect_right(list_a, 4))  # 4


# left_val <= x <= right_val 의 갯수를 O(logN) 시간에 구할 수 있는 함수
def count_by_range(data, left_val, right_val):
    right_idx = bisect_right(data, right_val)
    left_idx = bisect_left(data, left_val)
    return right_idx - left_idx


list_b = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print("4의 갯수:", count_by_range(list_b, 4, 4))  # 2
print("-1 <= x <= 3 인 x의 갯수:", count_by_range(list_b, -1, 3))  # 6

"""collections : deque같은 자료구조를 제공하는 라이브러리
deque : 파이썬에서 Queue를 구현할 때 사용하는 라이브러리
Queue 라이브러리가 존재하지만, 일반적인 Queue와 거리가 있으므로 deque를 사용하는 것이 좋다
"""

"""deque를 사용해야 하는 이유
python의 일반 리스트의 경우, 리스트 맨 앞에 원소를 추가하거나 제거하는데 O(N)의 시간복잡도가 소요된다
그러나 deque의 경우 O(1) 에 어떤 위치에서든 추가와 제거가 가능하다
"""
from collections import deque

queue = deque([2, 3, 4])
queue.append(5)
queue.appendleft(1)
queue.popleft()
queue.pop()
print(queue)  # [2, 3, 4]

"""Counter : 빈도 수를 세는 라이브러리
iterable 객체에서 객체 내부 원소가 몇 번 등장했는지 알려준다
"""
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])  # 3
print(counter['green'])  # 1
print(dict(counter))  # {'red': 2, 'blue': 3, 'green': 1}

"""math : 팩토리얼, 제곱근, 최대공약수(gcd) 등을 계산해주는 수학 라이브러리
factorial : 팩토리얼 (x!)
sqrt : 제곱근
gcd(a, b) : a와 b의 최대 공약수 반환
pi, e : 파이, 자연 상수 e
"""
import math

print(math.factorial(5))  # 120
print(int(math.sqrt(25)))  # 5
print(math.gcd(21, 14))  # 7
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
