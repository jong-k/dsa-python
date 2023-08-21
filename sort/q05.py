"""
p.360 안테나
백준 18310
"""
import sys
from math import floor

# \n 이나 " " 붙어있어도 int 래핑 가능
house_num = int(sys.stdin.readline())
house_list = [x for x in map(int, sys.stdin.readline().split())]
house_list.sort()
# 안테나를 집에만 설치할 수 있으므로 중위값을 출력
print(house_list[floor((house_num - 1) // 2)])
