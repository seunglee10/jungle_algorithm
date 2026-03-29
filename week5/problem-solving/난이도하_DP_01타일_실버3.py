# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

data = int(input())
dp = [0] * (data + 1)

if data >= 1:
    dp[1] = 1
if data >= 2:
    dp[2] = 2

for i in range(3, data + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[data])
