# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675


"""
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력

"""

data = "ABC"
count = 3

# count, data= input().split()

word = ""
for w in data:
    word += w * count
print(word)
