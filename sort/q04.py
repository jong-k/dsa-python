"""
p.359 국영수
백준 10825
"""
import sys

student_num = int(sys.stdin.readline().rstrip())
score_list = []
for _ in range(student_num):
    score_list.append(sys.stdin.readline().rstrip().split())

"""정렬 조건
국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
(단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
"""

# 조건의 우선순위가 낮은 순으로 정렬
score_list.sort(key=lambda x: x[0])
score_list.sort(key=lambda x: int(x[3]), reverse=True)
score_list.sort(key=lambda x: int(x[2]))
score_list.sort(key=lambda x: int(x[1]), reverse=True)

for i in range(student_num):
    print(score_list[i][0])
