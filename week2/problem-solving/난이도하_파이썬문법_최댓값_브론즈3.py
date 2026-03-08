# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562


"""
입력예제
3
29
38
12
57
74
40
85
61

출력예제
85
5

"""

# import sys
# data = list(map(int, sys.stdin.read().split()))

# data = [int(input()) for _ in range(9)]

data = [int(input()) for _ in range(9)]
max_number = data[0]
max_idx = 0
for idx, number in enumerate(data):
    if number > max_number:
        max_number = number
        max_idx = idx
print(max_number)
print(max_idx + 1)
