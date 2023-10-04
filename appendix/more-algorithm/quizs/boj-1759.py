"""
p.486 암호 만들기
백준 1759
"""

"""풀이
L, C = 암호 길이, 소문자 갯수 일 때
주어진 알파벳들을 정렬하고, L개를 뽑아 배열로 만든다
그리고 뽑은 배열에서 모음이 1개 이상, 자음이 2개 이상인 것들만 출력하면 된다
"""
from itertools import combinations

L, C = map(int, input().split())
arr = sorted(list(input().split()))
vowel_arr = ["a", "e", "i", "o", "u"]
for x in combinations(arr, L):
    vowel_num = 0
    for vowel in vowel_arr:
        if vowel in x:
            vowel_num += 1
    # 모음이 1개 이상, 모음 갯수가 전체 암호 길이-2 보다 작거나 같으면 됨
    if vowel_num >= 1 and L - vowel_num >= 2:
        print("".join(x))
