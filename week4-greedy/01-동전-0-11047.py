## Title: 동전 0
## Number: 11047
## Date: 2021.10.26

N, K = map(int, input().split())
coins = list()

for i in range(N):
	coins.append(int(input()))

result = 0
while len(coins) > 0:
	coin = coins.pop()
	result += K//coin
	K = K % coin

print(result)