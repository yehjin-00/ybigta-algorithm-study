## Title: 주유소
## Number: 13305
## Date: 2021.10.27

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]

result = 0
for i in range(len(road)):
	if price[i] < min_price: 
		min_price = price[i]
	result += min_price * road[i]

print(result)
