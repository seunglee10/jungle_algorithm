# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
# print(coins)

count = 0
for coin in coins[::-1]:
    if coin > k:
        pass
    elif coin <= k:
        count += k // coin
        k = k % coin
print(count)
