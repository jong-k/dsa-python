"""
p.375 금광
"""

input1 = ("2\n"
          "3 4\n"
          "1 3 3 2 2 1 4 1 0 6 4 7\n"
          "4 4\n"
          "1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2")

"""풀이
아래와 같은 3 * 4 2차원 리스트가 주어질 때,
     1  2  3  4
[   [1, 3, 3, 2],
    [2, 1, 4, 1], 
    [0, 6, 4, 7]    ]

dp(1) = 1열의 최댓값
dp(2)에서는, 2열에 올 수 있는 경우 중 최댓값을 반영해서 2열을 변경해준다
3에 올 수 있는 경우 중 최댓값 = max(1 + 3, 2 + 3)
1에 올 수 있는 경우 중 최댓값 = max(1 + 1, 2 + 1, 0 + 1)
6에 올 수 있는 경우 중 최댓값 = max(2 + 6, 0 + 6)

변경된 board, dp(2) = 8

     1  2  3  4
[   [1, 5, 3, 2],
    [2, 3, 4, 1], 
    [0, 8, 4, 7]    ]

"""


def dp(w, c, board):
    if c == 1:
        return max([board[i][0] for i in range(w)])
    for i in range(1, c):
        for j in range(w):
            if j == 0:
                board[j][i] += max(board[j][i - 1], board[j + 1][i - 1])
            elif j == w - 1:
                board[j][i] += max(board[j - 1][i - 1], board[j][i - 1])
            else:
                board[j][i] += max(board[j - 1][i - 1], board[j][i - 1], board[j + 1][i - 1])
    return max([board[i][c - 1] for i in range(w)])


def solution(data):
    data = data.split("\n")
    data_num = int(data[0])
    for i in range(1, 2 * data_num + 1, 2):
        row, column = map(int, data[i].split())
        data_array = list(map(int, data[i + 1].split()))
        array_list = [data_array[j:j + column] for j in range(0, len(data_array), column)]
        print(dp(row, column, array_list))


solution(input1)
