## Title: 연산자 끼워넣기
## Number: 14888
## Date: 2021.10.06

import itertools

num = int(input())
lst = list(map(int, input().split()))
operators = list(map(int, input().split()))
operator = []
for i in range(4):
	for j in range(operators[i]):
		operator.append(i)

combi = itertools.permutations(operator, num-1)
combi = list(set(combi))

value = []

for c in combi:
	result = lst[0]
	for i in range(len(c)):
		if c[i] == 0: result += lst[i+1]
		elif c[i] == 1: result -= lst[i+1]
		elif c[i] == 2: result *= lst[i+1]
		elif result < 0: result = -(abs(result)//lst[i+1])
		else: result = result//lst[i+1]
	value.append(result)

print(max(value))
print(min(value))