# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344



# data = map(int,input().split())


c = 5
data = [50, 50, 70, 80, 100]
student = []
average = sum(data) / len(data)
if data[i] >= average:
    