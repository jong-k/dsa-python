"""
p.180 성적이 낮은 순서로 학생 출력하기
"""
input1 = ("2\n"
          "홍길동 95\n"
          "이순신 77")


def solution(data):
    str_data = data.split("\n")
    student_num = int(str_data[0])
    score_list = []
    answer = ""
    for i in range(1, student_num + 1):
        name, score = str_data[i].split()
        score_list.append([name, int(score)])
    score_list.sort(key=lambda x: x[1])
    for score_info in score_list:
        answer += score_info[0] + " "
    return answer


print(solution(input1))
