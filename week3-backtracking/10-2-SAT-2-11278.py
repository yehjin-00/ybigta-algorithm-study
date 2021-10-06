## Title: 2-SAT-2
## Number: 11278
## Date: 2021.10.06

import itertools

N, M = map(int, input().split())

lst = []
for i in range(M): 
	lst.append(list(map(int, input().split())))

combi = ''
for i in range(2**N):
	case = '0'*(N-len(bin(i)[2:])) + bin(i)[2:]
	result = True
	for j in lst:
		left = bool(int(case[abs(j[0])-1]))
		right = bool(int(case[abs(j[1])-1]))
		if j[0] < 0: left = not left
		if j[1] < 0: right = not right
		if not left and not right: 
			result = False
			break
	if result: 
		combi = case
		break

if len(combi) > 0: 
	print(1)
	print(' '.join(combi))
else: print(0)