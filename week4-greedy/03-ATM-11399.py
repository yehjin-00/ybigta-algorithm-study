## Title: ATM
## Number: 11399
## Date: 2021.10.27

N = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)

result = 0
for idx, value in enumerate(lst):
	result += value * (len(lst)-idx)

print(result)