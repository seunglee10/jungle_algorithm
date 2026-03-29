# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541


n = input().strip()
parts = n.split("-")
# print(parts) # ['55', '50+40']

# 
first_sum = 0
save = 0
result = 0
part_sum = []
for part in parts:
    part_sum.append(sum(list(map(int, part.split("+")))))  # nums = [55], [50, 40]
    # print(part_sum) # [55, 90]
# print(part_sum)
result = part_sum[0]

for i in range(1,len(part_sum)):
    result -= part_sum[i]
        
print(result)
