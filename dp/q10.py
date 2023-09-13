"""
p.382 편집 거리
"""

"""풀이
2차원 리스트를 만들어서 dp를 실행

start text = cat
target text = cut

row = 타겟 텍스트 (cut)
col = 시작 텍스트 (cat)
              i                 j
memo[target length + 1][start length + 1] = start text의 i 인덱스까지 를 target text의 j 까지로 바꾸는데 필요한 편집 거리

   0 1 2 3
0    c a t
1  c 0 1 2
2  u 1 1 2
3  t 2 2 1
       ^
       |
       ca 를 cut로 바꾸는데 필요한 편집 거리 memo[3][2]
       
문자가 하나씩 추가되는 과정에서 계산!

점화식 세우기 
e.g. cat -> cut 일 때
1. 문자를 쌓아나갈 때 같은 문자열이면 이전과 비용 같음
cat -> cut == ca -> cu
즉, 추가되는 문자열이 같으면 memo[i][j] = memo[i - 1][j - 1]

e.g. ca -> cu 일 때 관련항을 아래로 대입할 수 있음
2. 삽입
c -> cu

3. 교체
ca -> cu

4. 삭제
ca -> c

"""


def solution(start_text, target_text):
    start_len = len(start_text)
    target_len = len(target_text)
    memo = [[0] * (start_len + 1) for _ in range(target_len + 1)]

    # 0열 초기화
    for i in range(target_len):
        memo[i + 1][0] = i + 1
    # 0행 초기화
    for i in range(start_len):
        memo[0][i + 1] = i + 1

    # memo 배열 채워나가기
    for i in range(1, target_len + 1):
        for j in range(1, start_len + 1):
            # 문자가 동일하다면 이전 단계와 동일
            if target_text[i - 1] == start_text[j - 1]:
                memo[i][j] = memo[i - 1][j - 1]
            # 문자가 동일하지 않으면 교체, 삭제, 삽입 중에서 최솟값 + 1
            else:
                memo[i][j] = 1 + min(memo[i - 1][j - 1], memo[i - 1][j], memo[i][j - 1])
    return memo[target_len][start_len]


print(solution("cat", "cut"))  # 1
print(solution("sunday", "saturday"))  # 3
