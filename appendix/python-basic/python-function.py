# 람다 표현식
def add(a, b):
    return a + b


print(add(1, 2))  # 3
# 즉시실행함수처럼 동작
print((lambda a, b: a + b)(1, 2))  # 3
