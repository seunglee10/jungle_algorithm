# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828


"""
명령의 수 14



"""

import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        stack.append(order[1])

    elif order[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif order[0] == "size":
        print(len(stack))

    elif order[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == "top":
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)
