"""
p.96 숫자 카드 게임
"""

"""
입력
3 3
3 1 2
4 1 4
2 2 2

출력
2

입력
2 4
7 3 1 8
3 3 3 4

출력
3
"""

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_num = 0

for row in board:
    max_num = max(max_num, min(row))

print(max_num)
