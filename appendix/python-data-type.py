# 실수 자료형

"""
e 다음에 오는 숫자는 10의 지수부를 의미한다
"""
num1 = 1e9  # 10의 9제곱
print(num1)  # 1000000000.0

num2 = 171.11e1
print(num2)  # 1711.1

num3 = 10e-3
print(num3)  # 0.01

"""
실수를 처리하기 위해 부동 소수점 방식을 사용하나,
컴퓨터의 한계로 이를 정확히 나타내지 못함
"""
print(0.3 + 0.6)  # 0.8999999999999999

# 리스트 자료형
"""
파이썬의 리스트는 연결 리스트 자료구조로 구현되어 있다
"""

"""
리스트 컴프리헨션
0부터 20까지 짝수만 담는 리스트 출력
"""
array1 = [i for i in range(1, 21) if i % 2 == 0]
# 아래와 동일
array2 = [i for i in range(2, 21, 2)]
print(array1)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(array2)

"""
5행 6열의 2차원 리스트 만들기
"""
list1 = [[0] * 6 for _ in range(5)]  # 반복을 위한 변수의 값을 무시할 때 언더바 _ 로 표현
print(list1)

"""리스트 관련 기타 메서드의 시간 복잡도
append : O(1)
sort : O(nlogn)
reverse : O(n)
insert(삽입할 인덱스, 삽입할 값) : O(n)
count : O(n)
remove(특정 값을 갖는 원소 하나를 제거) : O(n)
"""

"""
자연수 리스트에서 특정 값들을 모두 제거하기
"""
list_a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}  # set 자료구조

# remove_set에 없는 값만 저장
result_a = [i for i in list_a if i not in remove_set]
print(result_a)  # [1, 2, 4]

# 튜플 자료형

"""
한 번 선언되면 재할당이 불가능하다 (const)
또한 내부의 원소를 바꾸는 것도 불가능하다
리스트에 비해 공간 효율적이며, 각 원소의 성질이 서로 다를 때 주로 사용한다
"""

tuple1 = (1, 2, 3, 4)
print(tuple1[1])  # 2
# tuple1[1] = 5  # 에러 발생

# 딕셔너리 자료형

dict1 = {}
dict2 = dict()  # 이렇게도 선언 가능
dict1["사과"] = "apple"
dict1["토마토"] = "tomato"
dict2["포도"] = "grapes"
dict2["배"] = "pear"
print(dict1)  # {'사과': 'apple', '토마토': 'tomato'}
print(dict2)  # {'포도': 'grapes', '배': 'pear'}

# Set (집합) 자료형

"""
중복을 허용하지 않음
순서가 없음(인덱스로 참조 불가)
"""

set1 = {1, 2, 3, 3, 3}  # 중복된 원소는 제거됨
set2 = set([1, 2, 3, 3, 3])
print(set1)  # {1, 2, 3}
print(set2)  # {1, 2, 3}

set3 = {1, 3, 5}
# 합집합
print(set1 | set3)  # {1, 2, 3, 5}
# 교집합
print(set1 & set3)  # {1, 3}
# 차집합
print(set1 - set3)  # {2}

# 특정 값 하나 추가
set1.add(4)
print(set1)  # {1, 2, 3, 4}
# 여러 값 추가
set2.update([9, 10, 11])
print(set2)  # {1, 2, 3, 9, 10, 11}
# 특정 값 제거
set3.remove(1)
print(set3)  # {3, 5}
