# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157


"""
문제
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다

예제입력 1
Mississipi

예제출력 1
?
----------------
예제입력 2
zZa

예제출력 2
Z
---------------------
예제입력 3
baaa
예제출력
A
"""

data = "Mississipi"
alphabet = data.upper()
# print(alphabet) # MISSISSIPI
arr = [i for i in alphabet]

# print(arr)  # ['M', 'I', 'S', 'S', 'I', 'S', 'S', 'I', 'P', 'I']

# print(list(set(arr)))   # ['S', 'M', 'P', 'I']

alp = list(set(arr))

arr2 = []
for alpa in alp:
    arr2.append(arr.count(alpa))

# print(arr2) # [4, 4, 1, 1]

max_alpa = max(arr2)
count = arr2.count(max_alpa)
# print(max_alpa)  # 4
# print(count)    # 2
if count == 1:
    max_arr2_index = arr2.index(max_alpa)
    print(alp[max_arr2_index])
else:
    print("?")
