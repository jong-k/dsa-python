# 조건부 표현식
score = 85
result1 = "pass" if score >= 80 else "fail"
print(result1)  # pass
"""조건부 표현식의 활용
조건부 표현식은 리스트의 원소의 값을 변경해서 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용할 수 있다
"""

# 리스트에서 특정 값 빼기 (1) 기존 코드
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result2 = []
for i in a:
    if i not in remove_set:
        result2.append(i)
print(result2)  # [1, 2, 4]

# 조건부 표현식을 활용해 가독성 향상
result3 = [i for i in a if i not in remove_set]
print(result3)  # [1, 2, 4]

"""참고) Python에서는 조건문 안에서 수학적 부등식을 사용할 수 있다
x > 0 and x < 20 은 아래와 동일하다
0 < x < 20
"""
test = 60
if 0 < test < 100:
    print("OK")  # OK
