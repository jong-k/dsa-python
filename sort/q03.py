"""
p.182 두 배열의 원소 교체
"""

input1 = ("5 3\n"
          "1 2 5 4 3\n"
          "5 5 6 6 5")


def solution(data):
    data = data.split("\n")
    list_size, swap_count = map(int, data[0].split())
    list1 = sorted(map(int, data[1].split()))
    list2 = sorted(map(int, data[2].split()), reverse=True)
    for i in range(swap_count):
        if list1[i] < list2[i]:
            list1[i], list2[i] = list2[i], list1[i]
    return sum(list1)


print(solution(input1))  # 26
